from django.contrib import admin

from .models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información general', {
            'fields': ('title', 'author', 'description',),
        }),
        ('Foto', {
            'fields': ('image',),
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('status', 'slug',),
        }),
    )   

    list_display = ('title', 'author','status')
    list_filter = ('status',)
    search_fields = ['title', 'author']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Gallery, GalleryAdmin)