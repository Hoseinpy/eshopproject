from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.edit import CreateView
from account.models import User
from site_setting.models import BannerSetting
from utils.ip_service import user_claent_ip
from .forms import LoginForm, SingupForm, ProductForm, CommentForm, ProductFilterForm
from .models import Product, Comment, VisitedProduct
from django.views.decorators.csrf import csrf_exempt


class ProductListView(View):
    def get(self, request):
        filter_form = ProductFilterForm(request.GET or None)
        products_nw, products_fv = Product.objects.filter(newist_products=True).order_by('-created_at'), Product.objects.filter(favorite_products=True)
        num_of_product = Product.objects.all().count()
        banner = BannerSetting.objects.filter(is_active=True, position__exact=BannerSetting.BannerPosition.product_list)
        most_visit_product = Product.objects.filter(is_active=True).annotate(visit_count=Count('visitedproduct')).order_by('-visit_count')[:8]
        if filter_form.is_valid():
            category = filter_form.cleaned_data.get('category')
            products_nw, products_fv = products_nw.filter(category=category)[:8], products_fv.filter(category=category)[:8]
        return render(request, 'product/product_list.html', {
            'filter_form': filter_form,
            'products_nw': products_nw,
            'products_fv': products_fv,
            'num_of_product': num_of_product,
            'banner': banner,
            'most_visit_product': most_visit_product
        })


@method_decorator([login_required, csrf_exempt], name='dispatch')
class CreateProductView(CreateView):
    template_name = 'product/create_product.html'
    form_class = ProductForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProductDitealsView(View):
    def get(self, request, pk):
        comment_form = CommentForm()
        deatils = Product.objects.get(pk=pk)
        show_comment = Comment.objects.filter(product_id=pk).order_by('-created_at').exclude()
        comment_count = show_comment.count()

        user_ip = user_claent_ip(self.request)
        print(user_ip)
        has_been_visited = VisitedProduct.objects.filter(ip__iexact=user_ip, product_id=pk).exists()
        if not has_been_visited and self.request.user.is_authenticated:
            user_id = self.request.user.id
            new_visited = VisitedProduct(ip=user_ip, user_id=user_id, product_id=pk)
            new_visited.save()

        banner = BannerSetting.objects.filter(is_active=True, position__exact=BannerSetting.BannerPosition.product_details)
        print(request.POST)
        return render(request, 'product/product_deatls.html', {
            'deatils': deatils,
            'commentform': comment_form,
            'user_comment': show_comment,
            'comment_count': comment_count,
            'banner': banner
        })

    def post(self, request, pk):
        comment = CommentForm(request.POST or None)
        if comment.is_valid():
            product = Product.objects.get(pk=pk)
            comment = Comment(product_id=product, comment=request.POST.get('comment'))
            comment.save()
            return HttpResponseRedirect(str(pk))
        return render(request, 'product/product_deatls.html', {
            'commentform': comment
        })


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def get(self, request):
        login_from = LoginForm()
        return render(request, 'product/login.html', {
            'login_from': login_from
        })

    def post(self, request):
        login_from = LoginForm(request.POST)
        if login_from.is_valid():
            user: User = authenticate(request, username=login_from.cleaned_data.get('username'), password=login_from.cleaned_data.get('password'), email=login_from.cleaned_data.get('email'))
            if user is not None and user.is_active:
                login(request, user)
                return redirect(to=reverse('list'))
            else:
                login_from.add_error('username', 'مشخصات کاربری وارد شده یافت نشد')

        return render(request, 'product/login.html', {
            'login_from': login_from
        })


@method_decorator(csrf_exempt, name='dispatch')
class SingupView(View):
    def get(self, request):
        singup_form = SingupForm()
        return render(request, 'product/singup.html', {
            'singup_form': singup_form
        })

    def post(self, request):
        singup_form = SingupForm(request.POST)
        if singup_form.is_valid() and singup_form.cleaned_data.get('password') == singup_form.cleaned_data.get('confirm_password'):
            user_email = singup_form.cleaned_data.get('email')
            username_user = singup_form.cleaned_data.get('username')
            user = User.objects.filter(username__iexact=username_user).exists()
            if user:
                singup_form.add_error('username', 'نام کاربری یا ایمیل قبلا ثبت شده!')
            else:
                user = User.objects.filter(email__iexact=user_email).exists()
                if user:
                    singup_form.add_error('username', 'نام کاربری یا ایمیل قبلا ثبت شده!')
                else:
                    user: User = User.objects.create_user(username=username_user, email=user_email, email_verify_code=get_random_string(72), is_active=True)
                    user.set_password(singup_form.cleaned_data.get('password'))
                    user.save()
                    return redirect(reverse('login-page'))
        else:
            singup_form.add_error('confirm_password', 'رمز عبور با تکرار رمز عبور برابر نیست')

        return render(request, 'product/singup.html', {
            'singup_form': singup_form
        })

# برای تست بود
# # sandbox merchant
# if settings.SANDBOX:
#     sandbox = 'sandbox'
# else:
#     sandbox = 'www'
#
# ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
# ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
# ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"
#
# amount = 1000  # Rial / Required
# description = "نهایی کردن خرید شما از سایت ما"  # Required
# phone = ''  # Optional
# # Important: need to edit for realy server.
# CallbackURL = 'http://127.0.0.1:8080/verify/'
#
# def request_payment(request: HttpRequest):
#     data = {
#         "MerchantID": settings.MERCHANT,
#         "Amount": amount,
#         "Description": description,
#         "Phone": phone,
#         "CallbackURL": CallbackURL,
#     }
#     data = json.dumps(data)
#     # set content length by data
#     headers = {'content-type': 'application/json', 'content-length': str(len(data))}
#     try:
#         response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)
#
#         if response.status_code == 200:
#             response = response.json()
#             if response['Status'] == 100:
#                 return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']),
#                         'authority': response['Authority']}
#             else:
#                 return {'status': False, 'code': str(response['Status'])}
#         return response
#
#     except requests.exceptions.Timeout:
#         return {'status': False, 'code': 'timeout'}
#     except requests.exceptions.ConnectionError:
#         return {'status': False, 'code': 'connection error'}
#
#
# def verify_payment(request: HttpRequest):
#     pass


def loguots(request):
    logout(request)
    return redirect(to=reverse('login-page'))


def not_page(request):
    return render(request, 'product/404.html')
