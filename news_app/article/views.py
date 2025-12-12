from django.shortcuts import render, get_object_or_404
from django.views import View
from news_app.article.models import Article
from news_app.article.forms import TitleForm
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy


class IndexView(View):
    def get(self, request, *args, **kwargs):
        form = TitleForm(request.GET)
        if form.is_valid():
            title = form.cleaned_data["title"]
            if title != "":
                articles = Article.objects.filter(title__contains=title)
            else:
                articles = Article.objects.all()
        return render(
            request,
            "index.html",
            context={
                "articles": articles,
                "form": form,
            },
        )


class ArticleView(View):
    def get(self, request, article_id, *args, **kwargs):
        article = get_object_or_404(Article, id=article_id, is_published=True)
        return render(
            request,
            "article.html",
            context={
                "article": article,
            },
        )
