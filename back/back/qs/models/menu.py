from django.db import models
from .user import User
from .article import Article

class Menu(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    articles = models.ManyToManyField(Article)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
