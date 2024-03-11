from django.contrib import admin
from .models import SiteSetting, BannerSetting

# Register your models here.


@admin.register(BannerSetting)
class BannerSettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'is_active')


admin.site.register(SiteSetting)