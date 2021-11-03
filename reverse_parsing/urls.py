"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from reverse_parsing.views.redirect_view import redirect_register, register_post, register_success
from reverse_parsing.views.reverse_view import hello_reverse, welcome_reverse, show_hobby

app_name = "reverse_parsing"  # 这里即是第三步，设置 app_name

urlpatterns = [
    path('', hello_reverse),
    path('welcome-reverse/', welcome_reverse, name="hello_reverse"),
    path('reverse-with-param/<fruit>/<sport>.', show_hobby, name="hobby"),
    path('redirect-page/', redirect_register, name='register-page'),
    path('redirect-register/', register_post, name='register-form-post'),
    path('register-success/<username>', register_success, name='register-success')
]
