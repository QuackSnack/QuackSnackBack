from django.db import models
from .user import User

class Article(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
