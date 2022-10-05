from django.db import models
from .choice import Choice
from .tag import Tag


class Menu(models.Model):
  name = models.CharField(max_length=50)
  image = models.CharField(max_length=50)
  description = models.TextField()
  price = models.IntegerField()
  choice = models.ManyToManyField(Choice)
  tag = models.ManyToManyField(Tag)
  retaurant = models.ForeignKey('qs.User', on_delete=models.CASCADE)
