import json
from django.http import JsonResponse
from back.qs.serializers.user import UserSerializer
from back.qs.models.user import User
from back.qs.serializers.restaurant import RestaurantSerializer


def get_user(request, user_id=None):
  if request.method == 'GET':
    if user_id is None:
      try:
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
      except User.DoesNotExist:
        return JsonResponse({'message': "User not found"}, status=400)
    elif isinstance(user_id, int):
      try:
        user = User.objects.get(pk=user_id)
        serializer = UserSerializer(user)
      except User.DoesNotExist:
        return JsonResponse({'message': "User not found"}, status=400)
    return JsonResponse({'data': serializer.data})
  return JsonResponse({'message': "Wrong type of request"}, status=400)


def get_client(request, user_id=None):
  if request.method == 'GET':
    if user_id is None:
      try:
        user = User.objects.all().filter(role=0)
        serializer = UserSerializer(user, many=True)
      except User.DoesNotExist:
        return JsonResponse({'message': "User not found"}, status=400)
    elif isinstance(user_id, int):
      try:
        user = User.objects.get(pk=user_id, role=0)
        serializer = UserSerializer(user)
      except User.DoesNotExist:
        return JsonResponse({'message': "User not found"}, status=400)
    return JsonResponse({'data': serializer.data})
  return JsonResponse({'message': "Wrong type of request"}, status=400)


def get_restaurant(request, user_id=None):
  if request.method == 'GET':
    if user_id is None:
      try:
        user = User.objects.all().filter(role=1)
        serializer = RestaurantSerializer(user, many=True)
      except User.DoesNotExist:
        return JsonResponse({'message': "User not found"}, status=400)
    elif isinstance(user_id, int):
      try:
        user = User.objects.get(pk=user_id, role=1)
        serializer = RestaurantSerializer(user)
      except User.DoesNotExist:
        return JsonResponse({'message': "User not found"}, status=400)
    return JsonResponse({'data': serializer.data})
  return JsonResponse({'message': "Wrong type of request"}, status=400)


def modify_user(request, user_id=None):
  if request.method == 'POST':
    parameters = json.loads(request.body)
    if user_id is None:
      return JsonResponse({'message': "User not found"}, status=400)
    elif isinstance(user_id, int):
      try:
        user = User.objects.get(pk=user_id, role=1)
        if user.check_password(parameters['currentPassword']) and request.user.id == user_id:
          user.email = parameters['email']
          user.username = parameters['username']
          user.first_name = parameters['firstName']
          user.last_name = parameters['lastName']
          user.town = parameters['town']
          user.country = parameters['country']
          user.streetName = parameters['streetName']
          if parameters['newPassword'] != '':
            user.set_password(parameters['newPassword'])
          user.save()
          return JsonResponse({'message': "Restaurant modified"})
      except User.DoesNotExist:
        return JsonResponse({'message': "User not found"}, status=400)
    return JsonResponse({'message': "User not found"}, status=400)
  return JsonResponse({'message': "Wrong type of request"}, status=400)
