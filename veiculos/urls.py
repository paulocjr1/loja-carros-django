from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)