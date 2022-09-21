from rest_framework import serializers
from back.qs.serializers.article import ArticleSerializer
from back.qs.serializers.tag import TagSerializer
from back.qs.serializers.choice import ChoiceSerializer
from back.qs.models import Menu


class MenuSerializer(serializers.ModelSerializer):
  tag = TagSerializer(many=True)
  choice = ChoiceSerializer(many=True)
  # TODO make the tags dynamic
  # tag = articles

  class Meta:
    model = Menu
    fields = ('id', 'name', 'image', 'description', 'price', 'choice', 'tag', 'owner')
