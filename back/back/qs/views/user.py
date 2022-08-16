from django.http import JsonResponse
from back.qs.serializers.user import UserSerializer
from back.qs.models.user import User

def users(request):

    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return JsonResponse({'data' : serializer.data})


def user(request, user_id):

    user = User.objects.get(pk=user_id)
    serializer = UserSerializer(user)

    return JsonResponse(serializer.data)