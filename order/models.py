from django.db import models

from account.models import User
from product.models import Product


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='پرداخت شده / نشده')
    payment_date = models.DateField(verbose_name='تاریخ پرداخت', null=True, blank=True)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'

    def __str__(self):
        return str(self.user)


class OrderDeatils(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    quantity = models.IntegerField(verbose_name='تعداد')
    final_price = models.DecimalField(max_digits=20, decimal_places=0, verbose_name='قیمت نهایی', null=True, blank=True)

    class Meta:
        verbose_name = 'جزییات سبد خربد'
        verbose_name_plural = 'جزییات سبد های خربد'

    def __str__(self):
        return str(self.order)