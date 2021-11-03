from django.urls import path

from paginator_app.views import show_student


app_name = 'paginator_app'

urlpatterns = [
    path('', show_student)
]
