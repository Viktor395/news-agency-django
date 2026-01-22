from django.shortcuts import render, get_object_or_404
from .models import Article

def index(request):
    
    articles = Article.objects.all().order_by('-published_date')
    return render(request, 'news/index.html', {'articles': articles})

def article_detail(request, slug):
    
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'news/article_detail.html', {'article': article})
