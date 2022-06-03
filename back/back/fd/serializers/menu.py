from rest_framework import serializers
from back.fd.serializers.article import ArticleSerializer, ArticleSerializerFull
from back.fd.serializers.user import UserSerializer
from back.fd.models import Menu


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
