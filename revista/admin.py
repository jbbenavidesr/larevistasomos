from django.contrib import admin

from .models import Author, Category, Article, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'pub_date')
    list_filter = ('status','pub_date',)
    search_fields = ['title', 'body', 'author']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline]

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Article, ArticleAdmin)

