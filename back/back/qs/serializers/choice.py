from rest_framework import serializers
from back.qs.models.choice import Choice


class ChoiceSerializer(serializers.ModelSerializer):

  class Meta:
    model = Choice
    fields = ('id', 'name', 'possibilities')
