from django.shortcuts import render


def index(request):
    return render(request, 'revista/index.html')