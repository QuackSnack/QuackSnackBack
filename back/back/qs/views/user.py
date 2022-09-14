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
  users = User.objects.all()
  serializer = UserSerializer(users, many=True)
  return JsonResponse({'data': serializer.data})


def single_user(request, user_id):
  if request.method == 'GET' and request.user.id == user_id:
    user = User.objects.get(pk=user_id)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)


def all_client(request):
  clients = User.objects.filter(role=0)
  serializer = ClientSerializer(clients, many=True)
  return JsonResponse({'data': serializer.data})


def single_client(request, user_id):
  client = User.objects.filter(role=0).get(pk=user_id)
  serializer = ClientSerializer(client)
  return JsonResponse(serializer.data)


@requires_csrf_token
def all_restaurant(request):
  if request.user.is_authenticated:
    restaurants = User.objects.filter(role=1)
    serializer = RestaurantSerializer(restaurants, many=True)
    return JsonResponse({'data': serializer.data})
  else:
    return JsonResponse({'message': "User is not logged in"}, status=400)


def single_restaurant(request, user_id):
  restaurant = User.objects.filter(role=1).get(pk=user_id)
  serializer = RestaurantSerializer(restaurant)
  return JsonResponse(serializer.data)


# need to find a better solution
def all_data(request):
  if request.user.is_authenticated:
    restaurants = User.objects.filter(role=1)
    articles = Article.objects.all()
    menus = Menu.objects.all()
    srlz_restaurants = RestaurantSerializer(restaurants, many=True)
    srlz_articles = ArticleSerializer(articles, many=True)
    srlz_menus = MenuSerializer(menus, many=True)

    return JsonResponse({
        'restaurants': srlz_restaurants.data,
        'articles': srlz_articles.data,
        'menus': srlz_menus.data,
    })
  else:
    return JsonResponse({'message': "User is not logged in"}, status=400)
