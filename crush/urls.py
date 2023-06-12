# 引入path
from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'crush'

urlpatterns = [
    # 目前还没有urls
    path('login/', views.login_view, name='login'),
    path('add_crush/', views.add_crush, name='add_crush'),
    path('home/', views.home, name='home'),
    path('get_crush_info/', views.get_crush_info, name='get_crush_info'),
    path('get_user/', views.get_user, name='get_user'),
]