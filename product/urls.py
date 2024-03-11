from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('<int:pk>', views.ProductDitealsView.as_view(), name='deatls'),
    path('login/', views.LoginView.as_view(), name='login-page'),
    path('singup/', views.SingupView.as_view(), name='singup-page'),
    path('logouts/', views.loguots, name='logout-page'),
    path('not_found/', views.not_page, name='404-page'),
    path('create/', views.CreateProductView.as_view(), name='create-page'),
    # برای تست بود
    # path('request/', views.request_payment, name='request-page'),
    # path('verify/', views.verify_payment, name='verify-page'),
]