from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def static_welcome(request):
    return render(request, 'static_demo.html')


def register_ajax(request):
    return render(request, 'register_ajax.html')


def check_reg_name(request):
    reg_name = request.GET.get("reg_name")  # 接收 Ajax 请求。

    if reg_name != 'Emasik':  # 假设 Emasik 已经存在了。
        data = {
            "status": "1000",  # 状态码是随手定义的
            "msg": "恭喜，该用户名可用"
        }  # 这个写法是仿照常用的接口来做的。
    else:
        data = {
            "status": "1001",
            "msg": "哎，你这个名字已经被占用了"
        }
    return JsonResponse(data)
