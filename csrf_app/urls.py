from django.urls import path, include

from csrf_app.views import csrf_demo_page, csrf_register

app_name = 'csrf_app'


urlpatterns = [
    path('', csrf_demo_page, name='front-page-demo'),
    path('register/', csrf_register, name='register'),
]
