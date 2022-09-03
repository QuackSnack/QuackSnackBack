
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from back.qs.views.token import GetCSRFToken
from back.qs.views import  user, order, menu, article

from back.qs.viewset import vs_user, vs_article, vs_menu, vs_order

from rest_framework import views, serializers, status
from rest_framework.response import Response

class MessageSerializer(serializers.Serializer):
    message = serializers.CharField()
    
class EchoView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED)

router = routers.DefaultRouter()
router.register(r'users', vs_user.UserViewSet, basename='user')
router.register(r'clients', vs_user.ClientViewSet, basename='client')
router.register(r'restaurants', vs_user.RestaurantViewSet, basename='restaurant')
router.register(r'articles', vs_article.ArticleViewSet, basename='article')
router.register(r'orders', vs_order.OrderViewSet, basename='order')
router.register(r'menus', vs_menu.MenuViewSet, basename='menu')

urlpatterns = [
    path('tokenCSRF/', GetCSRFToken.as_view()),
    path('tokenJWT/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tokenJWT/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('get-all/user/', user.all_user, name='user'),
    path('get-all/client/', user.all_client, name='user'),
    path('get-all/restaurant/', user.all_restaurant, name='user'),
    path('get-all/article/', article.all_article, name='article'),
    path('get-all/menu/', menu.all_menu, name='menu'),
    path('get-all/order/', order.all_order, name='order'),
    
    path('get-single/user/<int:user_id>/', user.single_user, name='user'),
    path('get-single/client/<int:user_id>/', user.single_client, name='user'),
    path('get-single/restaurant/<int:user_id>/', user.single_restaurant, name='user'),
    path('get-single/article/<int:article_id>/', article.single_article, name='article'),
    path('get-single/menu/<int:menu_id>/', menu.single_menu, name='menu'),
    path('get-single/order/<int:order_id>/', order.single_order, name='order'),

    path('sign-in/', user.sign_in, name='sign_in'),
    path('sign-up/', user.sign_up, name='sign_up'),

    path('api/', include(router.urls)),

    path('', admin.site.urls), 
    
]