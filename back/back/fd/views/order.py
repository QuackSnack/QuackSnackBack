from django.http import JsonResponse
from back.fd.serializers.order import OrderSerializer, OrderSerializerFull
from back.fd.models.order import Order


def order(request, order_id):

    order = Order.objects.get(pk=order_id)
    serializer = OrderSerializer(order)

    return JsonResponse(serializer.data)

def order_full(request, order_id):

    order = Order.objects.get(pk=order_id)
    serializer = OrderSerializerFull(order)

    return JsonResponse(serializer.data)
