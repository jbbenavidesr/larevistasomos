from django.urls import path, include

from . import views

app_name = "revista"

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('archive/', views.IssueListView.as_view(), name='archive_index'),
    path('archive/<int:pk>/', views.ArchiveIndex.as_view(), name='archive_issue'),
    path('draft/<int:pk>/', views.DraftIndex.as_view(), name='draft'),
    path('archive/<slug:category>/',
         views.ArchiveCategory.as_view(), name='archive_category'),
    path('quien-somos/', views.AboutUs.as_view(), name='about_us'),
    path('autores/', views.AuthorList.as_view(), name='authors'),
    path('autores/<slug:author>/',
         views.AuthorArticleList.as_view(), name="author_list"),
    path('<slug:category>/', views.CategoryList.as_view(), name='category'),
    path('<slug:category>/<slug:slug>/',
         views.article_detail, name='article_detail'),
]
