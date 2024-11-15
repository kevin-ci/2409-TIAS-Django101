from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["headline", "author", "image", "copy"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author", "article", "text"]