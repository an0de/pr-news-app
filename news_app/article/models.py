from django.db import models
import django.contrib.auth.models as auth_models
from datetime import datetime as dt


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        auth_models.User, on_delete=models.CASCADE, related_name="user"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
