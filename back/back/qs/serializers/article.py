from rest_framework import serializers
from back.qs.models import Article
from back.qs.serializers.tag import TagSerializer


class ArticleSerializer(serializers.ModelSerializer):
  tag = TagSerializer(many=True)

  class Meta:
    model = Article
    fields = ('id', 'name', 'image', 'description', 'price', 'tag', 'owner')
