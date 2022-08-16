from django.http import JsonResponse
from back.qs.serializers.order import OrderSerializer, OrderSerializerFull
from back.qs.models.order import Order


def orders(request):

    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)

    return JsonResponse({'data' : serializer.data})


def order(request, order_id):

    order = Order.objects.get(pk=order_id)
    serializer = OrderSerializer(order)

    return JsonResponse(serializer.data)

def order_full(request, order_id):

    order = Order.objects.get(pk=order_id)
    serializer = OrderSerializerFull(order)

    return JsonResponse(serializer.data)
