from rest_framework import serializers
from back.qs.serializers.menu import MenuSerializer, MenuSerializerFull
from back.qs.serializers.article import ArticleSerializer, ArticleSerializerFull
from back.qs.serializers.user import UserSerializer
from back.qs.models import Order


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
