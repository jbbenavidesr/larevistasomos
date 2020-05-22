from django.urls import path

from . import views

app_name = "revista"

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('contact/', views.Contact, name='contact'),
    path('<slug:category>/', views.CategoryList.as_view(), name='category'),
    path('<slug:category>/<slug:slug>/', views.article_detail, name = 'article_detail'),
]
