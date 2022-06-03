from rest_framework import serializers
from back.qs.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'town', 'country', 'street', 'role', 'creation_date')
