from rest_framework import serializers
from back.qs.serializers.user import UserSerializer
from back.qs.serializers.menu import MenuSerializerFull
from back.qs.serializers.article import ArticleSerializer
from back.qs.models import User


class RestaurantSerializer(serializers.ModelSerializer):
  articles = ArticleSerializer(many=True)
  menus = MenuSerializerFull(many=True)

  class Meta:
    model = User
    fields = UserSerializer.Meta.fields + ('articles', 'menus')
