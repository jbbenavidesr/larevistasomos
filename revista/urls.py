from django.urls import path

from . import views

app_name = "revista"

urlpatterns = [
    path('', views.index.as_view(), name='home'),
    #path('<slug:slug>/', views.post_detail, name = 'post_detail'),
]
