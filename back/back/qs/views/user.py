from django.http import JsonResponse
from back.qs.serializers.user import UserSerializer
from back.qs.models.user import User
from django.http import *
import json
from django.contrib.auth import authenticate, login, logout
from back.qs.serializers.restaurant import RestaurantSerializer
from django.views.decorators.csrf import requires_csrf_token


def all_user(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse({'data': serializer.data})


def single_user(request, user_id):
    if request.method == 'GET':
        user = User.objects.get(pk=user_id)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)


@requires_csrf_token
def sign_in(request):
    if request.method == 'POST':
        try:
            parameters = json.loads(request.body)
            username = parameters['username']
            password = parameters['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("Logged in")
            return HttpResponse("User doesn't exists")
        except:
            return HttpResponse("Couldn't log in")


@requires_csrf_token
def sign_up(request):
    if request.method == 'POST':
        parameters = json.loads(request.body)
        if parameters['password'] == parameters['repeatedPassword']:
            user = User.objects.create_user(email=parameters['email'],
                                            username=parameters['username'],
                                            first_name=parameters['firstName'],
                                            last_name=parameters['lastName'],
                                            town=parameters['town'],
                                            country=parameters['country'],
                                            street=parameters['streetName'],
                                            role=parameters['role'])
            return HttpResponse("User created")
        return HttpResponse("User not created")


def all_client(request):
    clients = User.objects.filter(role=0)
    serializer = UserSerializer(clients, many=True)
    return JsonResponse({'data': serializer.data})


def single_client(request, user_id):
    client = User.objects.filter(role=0).get(pk=user_id)
    serializer = UserSerializer(client)
    return JsonResponse(serializer.data)


def all_restaurant(request):
    restaurants = User.objects.filter(role=1)
    serializer = RestaurantSerializer(restaurants, many=True)
    return JsonResponse({'data': serializer.data})


def single_restaurant(request, user_id):
    restaurant = User.objects.filter(role=1).get(pk=user_id)
    serializer = RestaurantSerializer(restaurant)
    return JsonResponse(serializer.data)
