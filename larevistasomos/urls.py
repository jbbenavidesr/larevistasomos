from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('cms/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('galeria/', include('gallery.urls')),
    path('', include('revista.urls')),
]

admin.site.site_header = "Administración Revista SOMOS"
admin.site.site_title = "Revista Somos Admin"
admin.site.index_title = "Bienvenido al portal Administrativo de la revista SOMOS"
