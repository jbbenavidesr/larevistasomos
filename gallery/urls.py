from django.contrib import admin
from django.urls import path

from .views import GalleryView, ImageView

app_name = "gallery"

urlpatterns = [
    path('', GalleryView.as_view(), name='gallery'),
    path('<slug:slug>', ImageView.as_view(), name='image'),
]