from django.contrib import admin
from django.urls import path, include
from news_app.article.views import IndexView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view()),
    path("articles/", include("news_app.article.urls")),
]
