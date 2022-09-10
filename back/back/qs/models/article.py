from django.db import models
from .tag import Tag

class Article(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    tag = models.ManyToManyField(Tag)
