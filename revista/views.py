import datetime

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.utils import timezone

from .models import Article, Comment, Category
from .forms import CommentForm


# def index(request):
#     return render(request, 'revista/index.html')

class Index(generic.ListView):
    template_name = 'revista/index.html'


    def get_queryset(self):
        """
        Return the articles in this edition (not including those set to be
        published in the future ). 
        """
        startdate = datetime.date(2020, 5, 1)
        enddate = timezone.now()
        return Article.objects.filter(
            pub_date__gte = startdate,
            pub_date__lte = enddate   
        ).order_by('-pub_date')
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['archive_post'] = Article.objects.filter(
            pub_date__lte = datetime.date(2020, 5, 1)
        ).order_by('-pub_date')[:3]
        return context

class CategoryList(generic.ListView):
    template_name = 'revista/index.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category'])
        return Article.objects.filter(
            category=self.category,
            pub_date__lte = timezone.now()  
        )
        
    queryset = get_queryset

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

def about_us(request):
    return render(request, 'about_us.html')