from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from pytils.translit import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    
    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    
    slug = models.SlugField(max_length=250, unique=True, blank=True, verbose_name="URL-адреса")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    content = models.TextField(verbose_name="Текст статті")
    image = models.ImageField(upload_to='news_images/', blank=True, verbose_name="Зображення")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публікації")

    class Meta:
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"
        ordering = ['-published_date']

    def save(self, *args, **kwargs):
        
        if not self.slug:
            
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        
        return reverse('article_detail', kwargs={'slug': self.slug})
