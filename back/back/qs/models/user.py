from django.db import models
from .article import Article
from .menu import Menu


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    role = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    articles = models.ManyToManyField(Article)
    menus = models.ManyToManyField(Menu)
