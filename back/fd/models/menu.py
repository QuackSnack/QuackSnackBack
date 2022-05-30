from django.db import models
from .user import User
from .article import Article

class Menu(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    articles_id = models.ManyToManyField(Article)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
