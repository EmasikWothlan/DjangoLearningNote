from django.urls import path, include

from ajax_play.views import ajax_play_front_page, ajax_play_trigger_ajax

app_name = 'ajax_play'


urlpatterns = [
    path('', ajax_play_front_page),
    path('ajax_play_trigger_ajax/', ajax_play_trigger_ajax, name='ajax_play_trigger_ajax')
]
