from django.db import models
from .article import Article


class Choice(models.Model):
  name = models.CharField(max_length=50)
  possibilities = models.ManyToManyField(Article)
