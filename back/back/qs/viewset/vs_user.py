from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from back.qs.models.user import User
from back.qs.serializers.user import UserSerializer


class UserViewSet(ViewSet):
  def list(self, request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, pk=None):
    queryset = User.objects.all()
    user = get_object_or_404(queryset, pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


class ClientViewSet(ViewSet):
  def list(self, request):
    queryset = User.objects.filter(role=0)
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, pk=None):
    queryset = User.objects.filter(role=0)
    user = get_object_or_404(queryset, pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


class RestaurantViewSet(ViewSet):
  def list(self, request):
    queryset = User.objects.filter(role=1)
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, pk=None):
    queryset = User.objects.filter(role=1)
    user = get_object_or_404(queryset, pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)
