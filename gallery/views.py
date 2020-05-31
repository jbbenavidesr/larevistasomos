from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Gallery

class GalleryView(generic.ListView):
    model =  Gallery
    template_name = "gallery/gallery.html"

class ImageView(generic.DetailView):
    model = Gallery
    template_name = "gallery/image.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

