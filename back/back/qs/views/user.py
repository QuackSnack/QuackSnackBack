from django.http import JsonResponse
from back.qs.models.article import Article
from back.qs.models.menu import Menu
from back.qs.serializers.article import ArticleSerializer
from back.qs.serializers.menu import MenuSerializer
from back.qs.serializers.user import UserSerializer
from back.qs.serializers.restaurant import RestaurantSerializer
from back.qs.serializers.client import ClientSerializer
from back.qs.models.user import User
from django.views.decorators.csrf import requires_csrf_token


def all_user(request):
  if request.method == 'GET':
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse({'data': serializer.data})
  return JsonResponse({'message': "Wrong type of request"}, status=400)


def single_user(request, user_id):
  if request.method == 'GET' and request.user.id == user_id:
    user = User.objects.get(pk=user_id)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)
  return JsonResponse({'message': "Wrong type of request"}, status=400)


def all_client(request):
  if request.method == 'GET':
    clients = User.objects.filter(role=0)
    serializer = ClientSerializer(clients, many=True)
    return JsonResponse({'data': serializer.data})
  return JsonResponse({'message': "Wrong type of request"}, status=400)


def single_client(request, user_id):
  if request.method == 'GET':
    client = User.objects.filter(role=0).get(pk=user_id)
    serializer = ClientSerializer(client)
    return JsonResponse(serializer.data)
  return JsonResponse({'message': "Wrong type of request"}, status=400)


@requires_csrf_token
def all_restaurant(request):
  if request.method == 'GET':
    if request.user.is_authenticated:
      restaurants = User.objects.filter(role=1)
      serializer = RestaurantSerializer(restaurants, many=True)
      return JsonResponse({'data': serializer.data})
    else:
      return JsonResponse({'message': "User is not logged in"}, status=400)
  return JsonResponse({'message': "Wrong type of request"}, status=400)


def single_restaurant(request, user_id):
  if request.method == 'GET':
    restaurant = User.objects.filter(role=1).get(pk=user_id)
    serializer = RestaurantSerializer(restaurant)
    return JsonResponse(serializer.data)
  return JsonResponse({'message': "Wrong type of request"}, status=400)
