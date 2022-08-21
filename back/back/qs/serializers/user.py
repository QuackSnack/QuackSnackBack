from rest_framework import serializers
from back.qs.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name',
                  'town', 'country', 'street', 'role', 'creation_date')


class RestaurantSerializerFull(serializers.ModelSerializer):
    #articles = ArticleSerializerFull()
    #menus = MenuSerializerFull()
    class Meta:
        model = User
        fields = UserSerializer.Meta.fields
