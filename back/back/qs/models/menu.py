from django.db import models
from .article import Article
from .tag import Tag


class Menu(models.Model):
  name = models.CharField(max_length=50)
  image = models.CharField(max_length=50)
  description = models.TextField()
  price = models.IntegerField()
  articles = models.ManyToManyField(Article)
  tag = models.ManyToManyField(Tag)
