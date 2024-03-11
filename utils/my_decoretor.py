from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse


def permision_cheking_for_user(func):
    def warpper(request: HttpRequest, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('login-page'))

    return warpper()