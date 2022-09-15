from django.http import JsonResponse
from back.qs.serializers.order import OrderSerializer
from back.qs.models.order import Order


def get_order(request, order_id=None):
  if request.method == 'GET':
    if order_id is None:
      try:
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
      except Order.DoesNotExist:
        return JsonResponse({'message': "order not found"}, status=400)
    elif isinstance(order_id, int):
      try:
        order = Order.objects.get(pk=order_id)
        serializer = OrderSerializer(order)
      except Order.DoesNotExist:
        return JsonResponse({'message': "order not found"}, status=400)
    return JsonResponse({'data': serializer.data})
  return JsonResponse({'message': "Wrong type of request"}, status=400)
