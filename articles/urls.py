from django.urls import path
from . import views

urlpatterns = [
    path("home", views.landing_page),
    path("<article_id>", views.view_article, name="view_article"),
]