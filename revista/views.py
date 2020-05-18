from django.shortcuts import render
from django.views import generic

from .models import Article


# def index(request):
#     return render(request, 'revista/index.html')

class index(generic.ListView):
    queryset = Article.objects.all()
    template_name = 'revista/index.html'