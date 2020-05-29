from django.urls import path, include

from . import views

app_name = "revista"

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('archive/', views.ArchiveIndex.as_view(), name='archive_index'),
    path('archive/<slug:category>/', views.ArchiveCategory.as_view(), name='archive_category'),
    path('quien-somos/', views.AboutUs.as_view(), name = 'about_us'),
    path('<slug:category>/', views.CategoryList.as_view(), name='category'),
    path('<slug:category>/<slug:slug>/', views.article_detail, name = 'article_detail'),
]
