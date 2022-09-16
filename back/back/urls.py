from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
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
    path('ping/', auth.ping, name='auth'),

    path('get/user/', user.get_user, name='user'),
    path('get/user/<int:user_id>/', user.get_user, name='user'),
    path('get/client/', user.get_client, name='user'),
    path('get/client/<int:user_id>/', user.get_client, name='user'),
    path('get/restaurant/', user.get_restaurant, name='user'),
    path('get/restaurant/<int:user_id>/', user.get_restaurant, name='user'),
    path('get/restaurant-and-articles/', user.get_restaurant, name='user'),
    path('get/restaurant-and-articles/<int:user_id>/', user.get_restaurant, name='user'),
    path('get/article/', article.get_article, name='article'),
    path('get/article/<int:article_id>/', article.get_article, name='article'),
    path('get/menu/', menu.get_menu, name='menu'),
    path('get/menu/<int:menu_id>/', menu.get_menu, name='menu'),
    path('get/order/', order.get_order, name='order'),
    path('get/order/<int:order_id>/', order.get_order, name='order'),

    path('modify/user/<int:user_id>/', user.modify_user, name='user'),

    path('create/article/', article.create_article, name='article'),

    path('check-user/<int:user_id>/', auth.check_user, name='check_user'),
    path('sign-in/', auth.sign_in, name='sign_in'),
    path('sign-up/', auth.sign_up, name='sign_up'),
    path('log-out/', auth.log_out, name='log_out'),

    path('api/', include(router.urls)),
    path('', admin.site.urls),
]
