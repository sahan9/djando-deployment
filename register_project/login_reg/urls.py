from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from login_reg import views


app_name = 'login_reg'

urlpatterns = [
    url('register/', views.register, name="register"),
    url('user_login/', views.user_login, name="user_login")
]
