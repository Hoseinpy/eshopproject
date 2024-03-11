from django.db import models

# Create your models here.


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100)
    site_address = models.CharField(max_length=100)
    site_domain = models.CharField(max_length=100)
    site_about = models.TextField(max_length=200)
    site_logo = models.ImageField(upload_to='files/site_logo')
    site_phone = models.CharField(max_length=20, blank=True, null=True)
    site_email = models.EmailField(max_length=100, blank=True, null=True)
    is_main_setting = models.BooleanField()

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return self.site_name


class BannerSetting(models.Model):
    class BannerPosition(models.TextChoices):
        product_list = 'product_list', 'صفحه لیست محصولات'
        product_details = 'product_details', 'صفحه جزییات محصولات'

    title = models.CharField(max_length=100, verbose_name='عنوان')
    url = models.URLField(verbose_name='ادرس')
    image = models.ImageField(upload_to='files/banner_image', verbose_name='عکس بنر')
    position = models.CharField(choices=BannerPosition.choices, max_length=200, verbose_name='محل قرار گیری')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')

    class Meta:
        verbose_name = 'لیست بنر'
        verbose_name_plural = 'لیست بنر ها'

    def __str__(self):
        return self.title