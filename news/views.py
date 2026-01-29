from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

def index(request):
    
    articles = Article.objects.all().order_by('-published_date')
    return render(request, 'news/index.html', {'articles': articles})

def article_detail(request, slug):
    
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'news/article_detail.html', {'article': article})

@login_required
def article_create(request):
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('index')
    else:
        form = ArticleForm()
    
    return render(request, 'news/article_form.html', {'form': form})