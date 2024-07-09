from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from products.views import home_page, news_page, not_found_page, search, product_page, add_product_to_cart, user_cart
from users.views import register_view, login_view, profile_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('about/', news_page), #HOMEWORK
    path("signup", register_view, name='signup'),
    path("login", login_view, name='login'),
    path("profile", profile_view, name='profile'),
    path("logout", logout_view, name='logout'),
    path("search", search),
    path("products/<int:id>", product_page),
    path("notfound", not_found_page, name="notfound"),
    path("add_to_cart/<int:id>", add_product_to_cart),
    path('user_cart', user_cart)
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)