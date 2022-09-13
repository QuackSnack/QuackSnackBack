from rest_framework import serializers
from back.qs.models import User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name',
              'town', 'country', 'street', 'role', 'avatar', 'banner', 'date_joined')
