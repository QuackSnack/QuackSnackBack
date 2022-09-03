from django.http import JsonResponse
from back.qs.serializers.user import UserSerializer
from back.qs.models.user import User
from django.http import *
import json
from django.contrib.auth import authenticate, login, logout
from back.qs.serializers.restaurant import RestaurantSerializer
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.sessions.models import Session


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
            user = authenticate(
                username=parameters['username'], password=parameters['password'])
            if user is not None:
                login(request, user)
                return JsonResponse({'message': "User logging in"})
            return JsonResponse({'message': "User not found"}, status=500)
        except:
            return JsonResponse({'message': "Couldn't log in"}, status=500)


@requires_csrf_token
def sign_up(request):
    if request.method == 'POST':
        parameters = json.loads(request.body)
        if parameters['password'] == parameters['repeatedPassword']:
            user = User.objects.create_user(email=parameters['email'],
                                            username=parameters['username'],
                                            password=parameters['password'],
                                            first_name=parameters['firstName'],
                                            last_name=parameters['lastName'],
                                            town=parameters['town'],
                                            country=parameters['country'],
                                            street=parameters['streetName'],
                                            role=parameters['role'])
            return JsonResponse({'message': "User created"})
        return JsonResponse({'message': "Couldn't create the user"}, status=500)


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
    s = Session.objects.get(pk=request.session.session_key)
    print(s.get_decoded())
    return JsonResponse({'data': serializer.data})

    
def single_restaurant(request, user_id):
    restaurant = User.objects.filter(role=1).get(pk=user_id)
    serializer = RestaurantSerializer(restaurant)
    return JsonResponse(serializer.data)
