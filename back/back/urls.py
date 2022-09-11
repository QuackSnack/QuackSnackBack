
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, views, serializers, status
from rest_framework.response import Response

from back.qs.views.token import GetCSRFToken
from back.qs.views import auth, user, order, menu, article
from back.qs.viewset import vs_user, vs_article, vs_menu, vs_order


router = routers.DefaultRouter()
router.register(r'users', vs_user.UserViewSet, basename='user')
router.register(r'clients', vs_user.ClientViewSet, basename='client')
router.register(r'restaurants', vs_user.RestaurantViewSet, basename='restaurant')
router.register(r'articles', vs_article.ArticleViewSet, basename='article')
router.register(r'orders', vs_order.OrderViewSet, basename='order')
router.register(r'menus', vs_menu.MenuViewSet, basename='menu')

urlpatterns = [
    path('tokenCSRF/', GetCSRFToken.as_view()),

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

    path('sign-in/', auth.sign_in, name='sign_in'),
    path('sign-up/', auth.sign_up, name='sign_up'),
    path('log-out/', auth.log_out, name='log_out'),

    path('api/', include(router.urls)),

    path('', admin.site.urls), 
]