from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from back.qs.models.order import Order
from back.qs.serializers.order import OrderSerializerFull


class OrderViewSet(ViewSet):
    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializerFull(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializerFull(order)
        return Response(serializer.data)