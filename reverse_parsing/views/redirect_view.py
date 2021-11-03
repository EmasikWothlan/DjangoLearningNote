from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse


def redirect_register(request):
    return render(request, "redirect_request/register.html")


def register_post(request):
    name = request.POST.get('username')
    # return render(request, 'redirect_request/register_success.html', {'registered_user': name})  # 转发
    # 直接返回上面这个页面不是不行，但是如果用户刷新这个页面就会导致重复提交，下面我们换一种方式
    return HttpResponseRedirect(reverse("reverse_parsing:register-success", args=(name,)))  # 重定向
    # return redirect(reverse("reverse_parsing:register-success", args=(name,)))  # 这个方法跟上面的是一样的


def register_success(request, username):
    registered_user = username
    return render(request, 'redirect_request/register_success.html', locals())
