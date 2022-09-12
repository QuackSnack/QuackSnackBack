from back.qs.models.user import User
from back.qs.serializers.user import UserSerializer
from django.http import *
import json
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.sessions.models import Session
from django.http import JsonResponse


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
      return JsonResponse({'message': "User created, try to log in"})
    return JsonResponse({'message': "Couldn't create the user"}, status=500)


@requires_csrf_token
def log_out(request):
  if request.method == 'POST':
    try:
      logout(request)
      return JsonResponse({'message': "User logged out"})
    except:
      return JsonResponse({'message': "Couldn't log out user"}, status=500)
