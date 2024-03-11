from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Todo)
class TodoAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass