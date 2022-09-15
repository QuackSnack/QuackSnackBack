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

    path('get/user/<int:user_id>/', user.get_user, name='user'),
    path('get/client/<int:user_id>/', user.get_client, name='user'),
    path('get/restaurant/<int:user_id>/', user.get_restaurant, name='user'),
    path('get/article/<int:article_id>/', article.get_article, name='article'),
    path('get/menu/<int:menu_id>/', menu.get_menu, name='menu'),
    path('get/order/<int:order_id>/', order.get_order, name='order'),

    path('create/article/<int:article_id>/', article.create_article, name='article'),
    path('create/menu/<int:menu_id>/', menu.create_menu, name='menu'),
    path('create/order/<int:order_id>/', order.create_order, name='order'),

    path('modify/user/<int:user_id>/', user.modify_user, name='user'),
    path('modify/article/<int:article_id>/', article.modify_article, name='article'),
    path('modify/menu/<int:menu_id>/', menu.modify_menu, name='menu'),
    path('modify/order/<int:order_id>/', order.modify_order, name='order'),
    
    path('delete/user/<int:user_id>/', user.delete_user, name='user'),
    path('delete/article/<int:article_id>/', article.delete_article, name='article'),
    path('delete/menu/<int:menu_id>/', menu.delete_menu, name='menu'),
    path('delete/order/<int:order_id>/', order.delete_order, name='order'),

    path('sign-in/', auth.sign_in, name='sign_in'),
    path('sign-up/', auth.sign_up, name='sign_up'),
    path('log-out/', auth.log_out, name='log_out'),

    path('api/', include(router.urls)),
    path('', admin.site.urls),
]
