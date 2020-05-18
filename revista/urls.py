from django.urls import path

from . import views

app_name = "revista"

urlpatterns = [
    path('', views.index, name='home')
]
