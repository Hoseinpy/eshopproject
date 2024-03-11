from django import forms
from .models import *


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'avatar', 'bio']

        labels = {'username': 'نام', 'avatar': 'عکس پروفایل', 'bio': 'بیو'}

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control'
            })}


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='کلمه عبور فعلی', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    new_password = forms.CharField(label='کلمه عبور جدید', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    confirm_password = forms.CharField(label='تکرار کلمه عبور', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))