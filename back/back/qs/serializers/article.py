from rest_framework import serializers
from back.qs.models import Article
from back.qs.serializers.user import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'name', 'image', 'description', 'price')
