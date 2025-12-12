from django.urls import path
from news_app.article.views import IndexView, ArticleView

urlpatterns = [
    path("", IndexView.as_view()),
    path("<int:article_id>", ArticleView.as_view(), name="article_info"),
]
