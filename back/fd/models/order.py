from django.db import models
from .user import User
from .article import Article
from .menu import Menu

class Order(models.Model):
    status = models.CharField(max_length=50)
    articles_id = models.ManyToManyField(Article)
    menus_id = models.ManyToManyField(Menu)
    date = models.DateTimeField(auto_now_add=True)
    cost = models.IntegerField()
    client = models.ForeignKey(User, on_delete=models.CASCADE)
