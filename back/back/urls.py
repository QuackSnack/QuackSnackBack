
from django.contrib import admin
from django.urls import path

from back.qs.views import user, order, menu, article

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<int:user_id>', user.user, name='user'),
    path('order/<int:order_id>', order.order, name='order'),
    path('order_full/<int:order_id>', order.order_full, name='order_full'),
    path('menu/<int:menu_id>', menu.menu, name='menu'),
    path('menu_full/<int:menu_id>', menu.menu_full, name='menu_full'),
    path('article/<int:article_id>', article.article, name='article'),
]
