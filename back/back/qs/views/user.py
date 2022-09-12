from django.http import JsonResponse
from back.qs.serializers.user import UserSerializer
from back.qs.serializers.restaurant import RestaurantSerializer
from back.qs.models.user import User
from rest_framework.permissions import IsAuthenticated


def all_user(request):
  users = User.objects.all()
  serializer = UserSerializer(users, many=True)
  return JsonResponse({'data': serializer.data})


def single_user(request, user_id):
  if request.method == 'GET':
    user = User.objects.get(pk=user_id)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)


def all_client(request):
  clients = User.objects.filter(role=0)
  serializer = UserSerializer(clients, many=True)
  return JsonResponse({'data': serializer.data})


def single_client(request, user_id):
  client = User.objects.filter(role=0).get(pk=user_id)
  serializer = UserSerializer(client)
  return JsonResponse(serializer.data)


def all_restaurant(request):
  if request.user.is_authenticated:
    restaurants = User.objects.filter(role=1)
    serializer = RestaurantSerializer(restaurants, many=True)
    return JsonResponse({'data': serializer.data})
  else:
    return JsonResponse({'message': "User is not logged in"}, status=500)


def single_restaurant(request, user_id):
  restaurant = User.objects.filter(role=1).get(pk=user_id)
  serializer = RestaurantSerializer(restaurant)
  return JsonResponse(serializer.data)
