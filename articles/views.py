from django.shortcuts import render, get_object_or_404
from .models import Article

def view_article(request, article_id):
    relevant_article = get_object_or_404(Article, id=article_id)

    context = { 
        "article": relevant_article, 
    }

    return render(request, 'articles/article.html', context)

def landing_page(request):
    all_articles = Article.objects.all()

    context = {
        "articles": all_articles,
    }

    return render(request, 'articles/index.html', context)