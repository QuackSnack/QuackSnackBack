from rest_framework import serializers
from back.qs.serializers.user import UserSerializer
from back.qs.models import User


class ClientSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = UserSerializer.Meta.fields
