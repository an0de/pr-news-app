from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils.crypto import pbkdf2
from datetime import datetime as dt
from news_app.article.models import Article

User.objects.all().delete()

User.objects.create(
    password=make_password("admin"),
    is_superuser=True,
    username="admin",
    last_name="",
    email="notset@example.com",
    is_staff=True,
    is_active=True,
    date_joined=dt.now(),
    first_name="",
)

user1 = User.objects.create(
    password=make_password("changeme"),
    is_superuser=False,
    username="user1",
    last_name="notset",
    email="notset@example.com",
    is_staff=False,
    is_active=False,
    date_joined=dt.now(),
    first_name="notset",
)

user2 = User.objects.create(
    password=make_password("changeme"),
    is_superuser=False,
    username="user2",
    last_name="",
    email="",
    is_staff=False,
    is_active=False,
    date_joined=dt.now(),
    first_name="",
)

Article.objects.create(
    title="News 1. Migration crysis",
    content="No migrations to apply.",
    author=user1,
)

Article.objects.create(
    title="News 2. Development server used in production",
    content="This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.",
    author=user2,
)

Article.objects.create(
    title="News 3. No issues identified",
    content="System check identified no issues.",
    author=user1,
)

Article.objects.create(
    title="News 4. Issues identified",
    content="System check identified issues.",
    author=user1,
    is_published=False,
)
