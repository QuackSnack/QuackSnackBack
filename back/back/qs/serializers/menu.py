from rest_framework import serializers
from back.qs.serializers.article import ArticleSerializer, ArticleSerializerFull
from back.qs.serializers.user import UserSerializer
from back.qs.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('name', 'image', 'description', 'price', 'articles', 'owner')


class MenuSerializerDetailed(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)
    owner = UserSerializer()
    class Meta:
        model = Menu
        fields = MenuSerializer.Meta.fields 


class MenuSerializerFull(serializers.ModelSerializer):
    articles = ArticleSerializerFull(many=True)
    owner = UserSerializer()
    class Meta:
        model = Menu
        fields = MenuSerializer.Meta.fields 
