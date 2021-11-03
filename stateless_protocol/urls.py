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
from django.urls import path

from stateless_protocol.views import add_cookie, remove_cookie, post_username, session_login, session_login_success, \
    session_delete_attribute, session_delete_session_and_cookie

app_name = 'stateless_protocol'


# /session/
urlpatterns = [
    # cookie 将 一段标识字符串 存在客户端，客户端通过在请求中带上这个字符串来让服务器识别身份
    path('add_cookie/', add_cookie, name='cookie_adding'),
    path('remove_cookie/', remove_cookie, name='cookie_removing'),
    path('post_username/', post_username, name='username_posting'),

    # 因为 cookie 的伪造难度较低，完全依靠客户端的信任，因此 session 放弃将标识字符串放在本地，转而将它放在服务器上
    path('session-login/', session_login, name='session_login'),
    path('session-login-success/', session_login_success, name='session_login_success'),
    path('session-delete-attribute/', session_delete_attribute, name='session_delete_attribute'),
    path('session-logout/', session_delete_session_and_cookie, name='session_logout'),

    # token 相比 Session，它更适合用在多服务器做 均衡负载 的场景下，因为用户每次请求可能会访问到不同的机器上，因此不能使用 session
    # token 相关的内容并没有听，留待之后。
]
