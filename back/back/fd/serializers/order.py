from rest_framework import serializers
from back.fd.serializers.menu import MenuSerializer, MenuSerializerFull
from back.fd.serializers.article import ArticleSerializer, ArticleSerializerFull
from back.fd.serializers.user import UserSerializer
from back.fd.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('status', 'articles', 'menus', 'date', 'cost', 'client')


class OrderSerializerDetailed(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)
    menus = MenuSerializer(many=True)
    client = UserSerializer()
    class Meta:
        model = Order
        fields = OrderSerializer.Meta.fields


class OrderSerializerFull(serializers.ModelSerializer):
    articles = ArticleSerializerFull(many=True)
    menus = MenuSerializerFull(many=True)
    client = UserSerializer()
    class Meta:
        model = Order
        fields = OrderSerializer.Meta.fields
