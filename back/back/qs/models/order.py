from django.db import models
from .user import User
from .article import Article
from .menu import Menu


class Order(models.Model):
  status = models.CharField(max_length=50)
  articles = models.ManyToManyField(Article)
  menus = models.ManyToManyField(Menu)
  date = models.DateTimeField(auto_now_add=True)
  cost = models.IntegerField()
  client = models.ForeignKey(User, related_name='client', on_delete=models.CASCADE)
  restaurant = models.ForeignKey(User, related_name='restaurant', on_delete=models.CASCADE)
