from django.db import models
from django.urls import reverse
from account.models import User
from jalali_date import datetime2jalali, date2jalali


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='نام دسته بندی', db_index=True)
    url_name = models.CharField(max_length=100, null=True, verbose_name='عنوان در url', db_index=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ManyToManyField(Category, verbose_name='دسته بندی')
    image = models.ImageField(upload_to='files/product', verbose_name='تصویر محصول', blank=True, null=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=0)
    description = models.TextField(max_length=500)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
    newist_products = models.BooleanField(default=True)
    favorite_products = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, db_index=True)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def get_jalali_created_date(self):
        return date2jalali(self.created_at)

    def get_jalali_created_time(self):
        return self.created_at.strftime('%H:%M')

    def get_absolute_url(self):
        return reverse('deatls', args=[self.pk])

    def __str__(self):
        return self.title


class Comment(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.TextField(max_length=500, verbose_name='کامنت', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'

    def get_jalali_created_time(self):
        return self.created_at.strftime('%H:%M')

    def __str__(self):
        return self.comment


class VisitedProduct(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='محصول', blank=True, null=True)
    ip = models.CharField(max_length=40, blank=True, null=True, verbose_name='ای پی کاربر')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدید های محصول'

    def __str__(self):
        return f'{self.product} ==>{self.ip}'