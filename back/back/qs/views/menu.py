from django.http import JsonResponse
from back.qs.serializers.menu import MenuSerializer
from back.qs.models.menu import Menu


def get_menu(request, menu_id=None):
  if request.method == 'GET':
    if menu_id is None:
      try:
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
      except Menu.DoesNotExist:
        return JsonResponse({'message': "menu not found"}, status=400)
    elif isinstance(menu_id, int):
      try:
        menu = Menu.objects.get(pk=menu_id)
        serializer = MenuSerializer(menu)
      except Menu.DoesNotExist:
        return JsonResponse({'message': "menu not found"}, status=400)
    return JsonResponse({'data': serializer.data})
  return JsonResponse({'message': "Wrong type of request"}, status=400)
