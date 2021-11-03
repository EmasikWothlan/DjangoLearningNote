from django.contrib import admin
from django.urls import path, include

from static_app.views import static_welcome, register_ajax, check_reg_name

app_name = 'static_app'

urlpatterns = [
    path('', static_welcome),
    path('register_ajax/', register_ajax),
    path("check/", check_reg_name, name='check_reg_name')
]
