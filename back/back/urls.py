
from django.contrib import admin
from django.urls import path

from back.qs.views import user, order, menu, article

urlpatterns = [
    path('admin/', admin.site.urls),

    path('users/', user.users, name='users'),
    path('user/<int:user_id>/', user.user, name='user'),

    path('articles/', article.articles, name='articles'),
    path('article/<int:article_id>/', article.article, name='article'),

    path('orders/', order.orders, name='orders'),
    path('order/<int:order_id>/', order.order, name='order'),
    path('order_full/<int:order_id>/', order.order_full, name='order_full'),

    path('menus/', menu.menus, name='menus'),
    path('menu/<int:menu_id>/', menu.menu, name='menu'),
    path('menu_full/<int:menu_id>/', menu.menu_full, name='menu_full'),
]
