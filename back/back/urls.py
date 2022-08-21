
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from back.qs.views import user, order, menu, article

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
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users/', user.users, name='users'),
    path('user/<int:user_id>/', user.user, name='user'),
    
    path('clients/', user.clients, name='clients'),
    path('client/<int:user_id>/', user.client, name='client'),
    
    path('restaurants/', user.restaurants, name='restaurants'),
    path('restaurant/<int:user_id>/', user.restaurant, name='restaurant'),

    path('articles/', article.articles, name='articles'),
    path('article/<int:article_id>/', article.article, name='article'),

    path('orders/', order.orders, name='orders'),
    path('order/<int:order_id>/', order.order, name='order'),
    path('order_full/<int:order_id>/', order.order_full, name='order_full'),

    path('menus/', menu.menus, name='menus'),
    path('menu/<int:menu_id>/', menu.menu, name='menu'),
    path('menu_full/<int:menu_id>/', menu.menu_full, name='menu_full'),

    path('api/', include(router.urls)),

    path('', admin.site.urls), 
    
]