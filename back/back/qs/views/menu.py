from django.http import JsonResponse
from back.qs.serializers.menu import MenuSerializer, MenuSerializerFull
from back.qs.models.menu import Menu


def menu(request, menu_id):

    menu = Menu.objects.get(pk=menu_id)
    serializer = MenuSerializer(menu)

    return JsonResponse(serializer.data)


def menu_full(request, menu_id):

    menu = Menu.objects.get(pk=menu_id)
    serializer = MenuSerializerFull(menu)

    return JsonResponse(serializer.data)