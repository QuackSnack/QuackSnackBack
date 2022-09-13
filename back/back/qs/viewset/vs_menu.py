from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from back.qs.models.menu import Menu
from back.qs.serializers.menu import MenuSerializer


class MenuViewSet(ViewSet):
  def list(self, request):
    queryset = Menu.objects.all()
    serializer = MenuSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, pk=None):
    queryset = Menu.objects.all()
    menu = get_object_or_404(queryset, pk=pk)
    serializer = MenuSerializer(menu)
    return Response(serializer.data)
