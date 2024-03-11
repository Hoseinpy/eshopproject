from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری', max_length=100, widget=forms.TextInput(attrs={
        'class': 'group-form',
        'placeholder': 'نام کاربری'
    }))
    password = forms.CharField(label='پسورد', max_length=30, widget=forms.PasswordInput(attrs={
        'class': 'group-form',
        'placeholder': 'پسورد'
    }))


class SingupForm(forms.Form):
    username = forms.CharField(label='نام کاربری', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'نام کاربری'
    }))
    password = forms.CharField(label='پسورد', max_length=30, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'پسورد'
    }))
    confirm_password = forms.CharField(label='تکرار پسورد', max_length=30, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'تکرار پسورد'
    }))

    email = forms.EmailField(label='ایمیل', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'ایمیل'
    }))


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'price', 'description']

        labels = {'category': 'دسته بندی', 'title': 'عنوان', 'image': 'تصویر محصول', 'price': 'قیمت', 'description': 'توضیحات'}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        labels = {'comment': 'کامنت'}

        widgets = {'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'نظر خود'})}


class ProductFilterForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True, label= 'دسته بندی', widget=forms.Select(attrs={
        'class': 'form-control',
        'placeholder': 'انتخاب فیلتر',
    }))

