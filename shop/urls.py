from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from products.views import home_page, about_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('about/', about_page)
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)