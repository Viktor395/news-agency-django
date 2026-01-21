from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Важливо, щоб назва була в лапках і точно збігалася
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
]