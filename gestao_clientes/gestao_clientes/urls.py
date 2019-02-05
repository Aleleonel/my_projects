from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path, include
from clientes import urls as clientes_urls
from produtos import urls as produtos_urls
from vendas import urls as vendas_urls
from home import urls as home_urls

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include(home_urls)),
    path('clientes/', include(clientes_urls)),
    path('produtos/', include(produtos_urls)),
    path('vendas/', include(vendas_urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


admin.site.site_header = 'Gestao de Clientes'
admin.site.index_title = 'Administracao'
admin.site.site_title = 'Seja bem vindo a BIT - Bionic Techno Info - Ltda'