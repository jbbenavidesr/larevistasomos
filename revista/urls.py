from django.urls import path

from . import views

app_name = "revista"

urlpatterns = [
    path('', views.index.as_view(), name='home'),
    path('<slug:category>/', views.category_list.as_view(), name='category'),
    path('<slug:category>/<slug:slug>/', views.article_detail, name = 'article_detail'),
]
