from django.http import JsonResponse
from back.qs.serializers.user import UserSerializer
from back.qs.models.user import User


def users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse({'data': serializer.data})


def user(request, user_id):
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
    serializer = UserSerializer(restaurants, many=True)
    return JsonResponse({'data': serializer.data})


def restaurant(request, user_id):
    restaurant = User.objects.filter(role=1).get(pk=user_id)
    serializer = UserSerializer(restaurant)
    return JsonResponse(serializer.data)


def restaurants(request):
    restaurants = User.objects.filter(role=1)
    serializer = UserSerializer(restaurants, many=True)
    return JsonResponse({'data': serializer.data})


def restaurant(request, user_id):
    restaurant = User.objects.filter(role=1).get(pk=user_id)
    serializer = UserSerializer(restaurant)
    return JsonResponse(serializer.data)
