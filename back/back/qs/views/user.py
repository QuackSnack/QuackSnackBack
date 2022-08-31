from django.http import JsonResponse
from back.qs.serializers.user import UserSerializer
from back.qs.models.user import User
from back.qs.serializers.restaurant import RestaurantSerializer
from django.views.decorators.csrf import requires_csrf_token


def users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse({'data': serializer.data})


@requires_csrf_token
def test(request):
    if request.method == 'POST':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse({'data': serializer.data})


def user(request, user_id):
    if request.method == 'GET':
        user = User.objects.get(pk=user_id)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)


def clients(request):
    clients = User.objects.filter(role=0)
    serializer = UserSerializer(clients, many=True)
    return JsonResponse({'data': serializer.data})


def client(request, user_id):
    client = User.objects.filter(role=0).get(pk=user_id)
    serializer = UserSerializer(client)
    return JsonResponse(serializer.data)


def restaurants(request):
    restaurants = User.objects.filter(role=1)
    serializer = RestaurantSerializer(restaurants, many=True)
    return JsonResponse({'data': serializer.data})


def restaurant(request, user_id):
    restaurant = User.objects.filter(role=1).get(pk=user_id)
    serializer = RestaurantSerializer(restaurant)
    return JsonResponse(serializer.data)
