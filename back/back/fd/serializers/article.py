from rest_framework import serializers
from back.fd.models import Article
from back.fd.serializers.user import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('name', 'image', 'description', 'price', 'owner')


class ArticleSerializerFull(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model = Article
        fields = ArticleSerializer.Meta.fields