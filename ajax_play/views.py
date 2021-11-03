from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def ajax_play_front_page(request):
    return render(request, 'ajax_play_front_page.html')


def ajax_play_trigger_ajax(request):
    data = {
        "something": "good"
    }
    return JsonResponse(data)

