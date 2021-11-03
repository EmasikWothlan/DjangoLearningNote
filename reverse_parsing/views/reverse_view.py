from django.http import HttpResponse
from django.shortcuts import render, reverse


def hello_reverse(request):
    # print(reverse("reverse_parsing:hello_reverse"))
    return render(request, "reverse_parsing/reverse_parse_url.html")


def welcome_reverse(request):
    return HttpResponse("<h3 style='color:green'> Hello, reverse_url </h3>")


def show_hobby(request, fruit, sport):
    msg = f"喜欢的水果是{fruit}，喜欢的运动是{sport}"
    return HttpResponse(f'<h3> {msg} </h3>')
