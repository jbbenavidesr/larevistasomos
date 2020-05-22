from django.contrib import admin

from .models import Author, Category, Article, Comment, Image

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ImageInline(admin.TabularInline):
    model = Image
    extra = 2

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información general', {
            'fields': ('title', 'author', 'description', 'pub_date', 'category',),
        }),
        ('Contenido', {
            'fields': ('body', 'bib',),
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('status', 'slug', 'claps','template_name',),
        }),
    )   

    list_display = ('title', 'author', 'category', 'pub_date', 'status')
    list_filter = ('status','pub_date',)
    search_fields = ['title', 'body', 'author']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ImageInline, CommentInline]

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name',),
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('slug',),
        }),
    )
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Author)
admin.site.register(Article, ArticleAdmin)

