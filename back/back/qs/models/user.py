from django.db import models
from .article import Article
from .menu import Menu
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  town = models.CharField(max_length=30, null=True)
  country = models.CharField(max_length=30, null=True)
  street = models.CharField(max_length=30, null=True)
  role = models.IntegerField(null=True)
  articles = models.ManyToManyField(Article)
  menus = models.ManyToManyField(Menu)
