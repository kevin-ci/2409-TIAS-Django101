from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def view_article(request, article_id):
    relevant_article = get_object_or_404(Article, id=article_id)
    form = CommentForm()
    comments = relevant_article.comments


    context = { 
        "article": relevant_article,
        "comment_form": form,
        "comments": comments, 
    }

    return render(request, 'articles/article.html', context)

def landing_page(request):
    all_articles = Article.objects.all()

    context = {
        "articles": all_articles,
    }

    return render(request, 'articles/index.html', context)

def add_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment successfully created.")
            return redirect('home')
    return redirect('home')

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        messages.error(request, "You cannot edit a comment that is not yours!")
        return redirect('home')
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment successfully updated.")
            return redirect('home')
        else:
            return redirect('home')
    else:
        form = CommentForm(instance=comment)
        context = {
            "form": form,
        }
        return render(request, 'articles/edit_comment.html', context)

@staff_member_required
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Article successfully created.")
            return redirect('home')
        else:
            return redirect('create_article')
    else:
        form = ArticleForm()
        context = {
            "form": form,
        }
        return render(request, 'articles/create_article.html', context)

@staff_member_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Article successfully updated.")
            return redirect('home')
        else:
            return redirect('create_article')
    else:
        form = ArticleForm(instance=article)
        context = {
            "form": form,
        }
        return render(request, 'articles/edit_article.html', context)

@staff_member_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        article.delete()
        messages.success(request, "Article successfully deleted.")
        return redirect("home")
    else:
        return render(request, 'articles/delete_article.html')