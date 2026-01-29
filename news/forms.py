from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        
        fields = ['title', 'category', 'image', 'content']
        
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введіть заголовок новини'}),
            'content': forms.Textarea(attrs={'placeholder': 'Напишіть текст статті тут...'}),
        }