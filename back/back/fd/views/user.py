from django.http import JsonResponse
from back.fd.serializers.user import UserSerializer
from back.fd.models.user import User


def user(request, user_id):

    user = User.objects.get(pk=user_id)
    serializer = UserSerializer(user)

    return JsonResponse(serializer.data)