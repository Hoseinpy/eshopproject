from django import template
from jalali_date import date2jalali, datetime2jalali

register = template.Library()


@register.filter(name='show_date_jalali')
def show_jalali_date(value):
    return date2jalali(value)


@register.filter(name='show_time_jalali')
def show_jalali_time(value):
    return datetime2jalali(value)


@register.filter(name='threy_digits_currency')
def threy_digits_currency(value):
    return '{:,}'.format(value)