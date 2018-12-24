from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path, include
from clientes import urls as clientes_urls
from home import urls as home_urls

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', include(home_urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('clientes/', include(clientes_urls) ),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


