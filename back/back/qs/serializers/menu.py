from rest_framework import serializers
from back.qs.serializers.article import ArticleSerializer
from back.qs.serializers.user import UserSerializer
from back.qs.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'image', 'description', 'price', 'articles')


class MenuSerializerFull(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)
    class Meta:
        model = Menu
        fields = MenuSerializer.Meta.fields 
