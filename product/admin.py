from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'price', 'author', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['id', 'title']

    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         obj.author = request.user
    #     return super().save_model(request, obj, form, change)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(models.VisitedProduct)
class VisitedProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'ip', 'product']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass