from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.static import serve
from core.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Home
    path('veiculos/', include('catalogo.urls')),  # adiciona as rotas do app
    path('painel/', include('painel.urls')),
    path("login/", auth_views.LoginView.as_view(template_name="painel/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('financiamento/', include('financiamento.urls')),
    path('vendas/', include('vendas.urls')),
]

handler404 = 'core.views.page_not_found'

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^veiculos/imagens/(?P<path>.*)$', serve, {
            'document_root': settings.BASE_DIR / 'veiculos' / 'imagens',
        }),
        re_path(r'^uploads/veiculos/(?P<path>.*)$', serve, {
            'document_root': settings.BASE_DIR / 'uploads' / 'veiculos',
        }),
    ]
    urlpatterns += [re_path(r'^(?P<unmatched_path>.*)$', page_not_found)]
