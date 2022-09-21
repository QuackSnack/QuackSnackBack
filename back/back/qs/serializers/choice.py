from rest_framework import serializers
from back.qs.serializers.article import ArticleSerializer
from back.qs.models.choice import Choice


class ChoiceSerializer(serializers.ModelSerializer):
  possibilities = ArticleSerializer(many=True)

  class Meta:
    model = Choice
    fields = ('id', 'name', 'possibilities')
