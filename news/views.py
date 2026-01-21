from django.shortcuts import render, get_object_or_404 # Додали get_object_or_404
from .models import Article

def index(request):
    # Отримуємо всі статті, від нових до старих
    articles = Article.objects.all().order_by('-published_date')
    return render(request, 'news/index.html', {'articles': articles})

def article_detail(request, slug):
    # Ця функція шукає статтю за її "slug". 
    # Якщо не знайде — видасть помилку 404 (сторінка не знайдена).
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'news/article_detail.html', {'article': article})
