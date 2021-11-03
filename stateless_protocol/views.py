import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


# set cookie.
def add_cookie(request):
    try:
        username = request.get_signed_cookie('username', salt='123654')
    except:
        pass
    return render(request, 'adding_cookies_demo.html', locals())


def remove_cookie(request):
    response = HttpResponse('<h3>cookie has been removed</h3>')
    response.delete_cookie("username")  # it sets named cookie expired. consider it as set_cookie(expire=1970.01.01).
    return response


def post_username(request):
    response = HttpResponseRedirect(reverse('session_app:cookie_adding'))
    username = request.POST.get('username')
    # if set any utf-8 character in cookie, you have to change headers.py encoding into "utf-8", or it'll go wrong.
    response.set_signed_cookie('username', username, salt='123654')
    return response


# set session.
def session_login(request):
    # different method would shift this view function's behavior. Using same URL.
    if request.method == "GET":
        return render(request, "session_login_demo.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        if username == "Emasik":
            request.session['username'] = "Emasik"
            return redirect(reverse("stateless_protocol:session_login_success"))
        else:
            return redirect(reverse("stateless_protocol:session_login"))


def session_login_success(request):
    return render(request, "session_login_success.html")


def session_delete_attribute(request):
    print(f"username: {request.session['username']}")
    del request.session['username']  # 不知为何不能使用 request.session.delete() 方法来删除它
    return HttpResponse("<h3> username 已经被删除了 </h3>")


def session_delete_session_and_cookie(request):
    request.session.flush()
    return HttpResponse("<h3> 您已登出 </h3>")


# 这里开始就是 token 了。


