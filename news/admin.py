from django.contrib import admin
from .models import Category, Article

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)} # Автоматично пише slug з імені

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # Що ми бачимо в списку новин
    list_display = ('title', 'category', 'author', 'published_date')
    # Фільтри справа
    list_filter = ('category', 'author', 'published_date')
    # Пошук по заголовку та тексту
    search_fields = ('title', 'content')
    # Автоматичний slug з заголовка
    prepopulated_fields = {'slug': ('title',)}
    # Зручний інтерфейс для вибору дати
    date_hierarchy = 'published_date'
