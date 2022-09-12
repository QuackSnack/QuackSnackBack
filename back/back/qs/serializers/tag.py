from rest_framework import serializers
from back.qs.models.tag import Tag


class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ('name',)
