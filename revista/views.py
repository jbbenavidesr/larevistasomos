from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Article, Comment, Category
from .forms import CommentForm


# def index(request):
#     return render(request, 'revista/index.html')

class Index(generic.ListView):
    queryset = Article.objects.all()
    template_name = 'revista/index.html'

class CategoryList(generic.ListView):
    template_name = 'revista/index.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category'])
        return Article.objects.filter(category=self.category)
        
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