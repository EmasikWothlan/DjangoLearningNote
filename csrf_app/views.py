from django.shortcuts import render


# Create your views here.
def csrf_demo_page(request):
    return render(request, "csrf_demo.html")


def csrf_register(request):
    username = request.POST.get("username")
    return render(request, 'login.html', locals())

