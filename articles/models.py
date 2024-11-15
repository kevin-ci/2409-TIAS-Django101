from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    headline = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    image = models.URLField()
    copy = models.TextField()

    def __str__(self):
        return self.headline

class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()