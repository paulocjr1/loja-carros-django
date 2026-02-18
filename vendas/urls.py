from django.urls import path
from . import views

urlpatterns = [
    path('enviar/', views.enviar_veiculo, name='enviar_veiculo'),
    path('sucesso/', views.venda_sucesso, name='venda_sucesso'),
]
