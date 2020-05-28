from django.contrib import admin
from django.urls import path

from .views import contactView, SuccessView

app_name = "contact"

urlpatterns = [
    path('', contactView, name='contact'),
    path('success/', SuccessView.as_view(), name='success'),
]