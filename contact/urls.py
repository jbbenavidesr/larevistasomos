from django.contrib import admin
from django.urls import path

from .views import contactView, successView

app_name = "contact"

urlpatterns = [
    path('', contactView, name='contact'),
    path('success/', successView, name='success'),
]