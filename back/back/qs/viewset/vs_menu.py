from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from back.qs.models.menu import Menu
from back.qs.serializers.menu import MenuSerializerFull


class MenuViewSet(ViewSet):
  def list(self, request):
    queryset = Menu.objects.all()
    serializer = MenuSerializerFull(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, pk=None):
    queryset = Menu.objects.all()
    menu = get_object_or_404(queryset, pk=pk)
    serializer = MenuSerializerFull(menu)
    return Response(serializer.data)
