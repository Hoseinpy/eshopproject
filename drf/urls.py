from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('', views.TodoViewSetApiView)

urlpatterns = [
    path('todo/', views.TodoManageApiView.as_view(), name='todo_seri-page'),
    path('todo/<int:todo_id>', views.TodoDetailApiView.as_view(), name='todo_detail-page'),
    path('mixin/', views.TodoListMixinsApiView.as_view(), name='todo_seri-page'),
    path('mixin/<int:pk>', views.TodoDetailMixinsApiView.as_view(), name='todo_seri-page'),
    path('generic/', views.TodoGenericsApiView.as_view(), name='todo_seri-page'),
    path('generic/<int:pk>', views.TodoDetailGenericApiView.as_view(), name='todo_seri-page'),
    path('viewset/', include(router.urls)),
    path('users/', views.UserGenericsApiView.as_view(), name='ghsdhicg'),
    path('users/<int:pk>', views.UserDetailGenericsApiView.as_view(), name='ghsdhicg'),
    path('auth-token/', obtain_auth_token, name='generate-auth-token'),
    path('currency-list/', views.CurrencyListApiView.as_view(), name='currency-list'),
    path('currency-list/<str:symbol>', views.CurrencySymbol.as_view(), name='currency-list'),

]