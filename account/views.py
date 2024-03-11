from django.views.generic import TemplateView, View
from .forms import EditProfileForm, ChangePasswordForm
from account.models import User
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.
@method_decorator(login_required, name='dispatch')
class UserPannelView(TemplateView):
    template_name = 'account/user_pannel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        current_user = User.objects.filter(id=request.user.id).first()
        context['current_user'] = current_user

        return context


@method_decorator(login_required, name='dispatch')
class EditProfileView(View):
    def get(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileForm(instance=current_user)
        return render(request, 'account/edit_profile.html', {
            'edit_form': edit_form,
            'current_user': current_user
        })

    def post(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
            return redirect(reverse('user-pannel-page'))

        return render(request, 'account/edit_profile.html', {
            'edit_form': edit_form,
        })


@method_decorator(login_required, name='dispatch')
class ChangePasswordView(View):
    def get(self, request):
        change_form = ChangePasswordForm()
        return render(request, 'account/change_password.html', {
            'change_form': change_form
        })

    def post(self, request):
        change_form = ChangePasswordForm(request.POST)
        if change_form.is_valid() and change_form.cleaned_data.get('new_password') == change_form.cleaned_data.get('confirm_password'):
            current_user = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(change_form.cleaned_data.get('old_password')):
                current_user.set_password(change_form.cleaned_data.get('new_password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login-page'))
            else:
                change_form.add_error('old_password', 'رمز عبور فعلی وارد شده اشتباه می باشد')
        else:
            change_form.add_error('confirm_password', 'تکرار رمز عبور وارد شده اشتباه می باشد')

        return render(request, 'account/change_password.html', {
            'change_form': change_form
        })