"""djangoLearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', v_count)
    path('reverse-parse-url/', include('reverse_parsing.urls', namespace='reverse_parsing')),
    # namespace 的目的就是替代总路由中的这一段 url 片段。
    path('static_app/', include('static_app.urls', namespace='static_app')),
    path('csrf_app/', include('csrf_app.urls', namespace='csrf_app')),
    path('ajax_play/', include('ajax_play.urls', namespace='ajax_play')),
    path('sessions/', include('stateless_protocol.urls', namespace='session_app')),

    # paginator
    path('paginator/', include('paginator_app.urls', namespace='paginator_app')),
]
