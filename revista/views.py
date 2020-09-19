import datetime

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.utils import timezone

from .models import Article, Comment, Category, Author
from .forms import CommentForm
from gallery.models import Gallery


class Index(generic.ListView):
    template_name = 'revista/index.html'
    startdate = datetime.date(2020, 5, 1)
    enddate = timezone.now()

    def get_queryset(self):
        """
        Return the articles in this edition (not including those set to be
        published in the future ). 
        """
        
        return Article.objects.filter(
            issue__current=True  
        ).exclude(
            category__slug = 'cuentos'
        ).exclude(
            category__slug = 'poemas'
        ).order_by('-pub_date', '-update')
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['archive_post'] = Article.objects.filter(
            pub_date__lte = datetime.date(2020, 5, 1)
        ).order_by('-pub_date')[:3]

        context['cuentos'] = Article.objects.filter(
            category__slug = 'cuentos',
            pub_date__gte = self.startdate,
            pub_date__lte = self.enddate  
        )

        context['poemas'] = Article.objects.filter(
            category__slug = 'poemas',
            pub_date__gte = self.startdate,
            pub_date__lte = self.enddate  
        )

        context['gallery'] = Gallery.objects.order_by('?')[:10]
        
        return context

class ArchiveIndex(generic.ListView):
    template_name = 'revista/index.html'
    enddate = datetime.date(2020, 5, 1)

    def get_queryset(self):
        """
        Return the articles in this edition (not including those set to be
        published in the future ). 
        """
        
        return Article.objects.filter(
            pub_date__lte = self.enddate   
        ).exclude(
            category__slug = 'cuentos'
        ).exclude(
            category__slug = 'poemas'
        ).order_by('-pub_date')
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['archive_post'] = Article.objects.filter(
            pub_date__lte = datetime.date(2020, 5, 1)
        ).order_by('-pub_date')[:3]

        context['cuentos'] = Article.objects.filter(
            category__slug = 'cuentos',
            pub_date__lte = self.enddate  
        )

        context['poemas'] = Article.objects.filter(
            category__slug = 'poemas',
            pub_date__lte = self.enddate  
        )
        return context


class CategoryList(generic.ListView):
    template_name = 'revista/category_list.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category'])
        startdate = datetime.date(2020, 5, 1)
        enddate = timezone.now()
        return Article.objects.filter(
            category= self.category,
            pub_date__gte = startdate,
            pub_date__lte = enddate  
        )
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['archive_post'] = Article.objects.filter(
            pub_date__lte = datetime.date(2020, 5, 1),
            category = self.category
        ).order_by('-pub_date')[:3]

        context['category'] = self.category

        return context

class ArchiveCategory(generic.ListView):
    template_name = 'revista/archive_category.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category'])
        enddate = datetime.date(2020, 5, 1)
        return Article.objects.filter(
            category= self.category,
            pub_date__lte = enddate  
        )
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['archive_post'] = Article.objects.filter(
            pub_date__gte = datetime.date(2020, 5, 1),
            pub_date__lte = timezone.now(),
            category = self.category
        ).order_by('-pub_date')[:3]

        context['category'] = self.category

        return context

class AuthorList(generic.ListView):
    model = Author
    template_name = "revista/authors.html"

class AuthorArticleList(generic.ListView):
    template_name = 'revista/author_list.html'

    def get_queryset(self):
        self.author = get_object_or_404(Author, slug=self.kwargs['author'])
        enddate = timezone.now()
        return Article.objects.filter(
            author= self.author,
            pub_date__lte = enddate  
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add the author
        context['author'] = self.author

        return context

def article_detail(request, category, slug):
    article = get_object_or_404(Article, slug=slug)
    template_name = 'revista/' + article.template_name
    comments = article.comments.filter(active = True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit = False)
            # Assign the current post to the comment
            new_comment.article = article
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, { 'article': article,
                                            'comments': comments,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form})

class AboutUs(generic.TemplateView):
	template_name = 'about-us.html'