from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPannelView.as_view(), name='user-pannel-page'),
    path('edit_profile', views.EditProfileView.as_view(), name='edit-profile-page'),
    path('change_password', views.ChangePasswordView.as_view(), name='change_password-page'),
]