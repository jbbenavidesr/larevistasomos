from django.urls import path

from . import views

app_name = "revista"

urlpatterns = [
    path('', views.index.as_view(), name='home'),
    path('<slug:slug>/', views.article_detail, name = 'article_detail'),
]
