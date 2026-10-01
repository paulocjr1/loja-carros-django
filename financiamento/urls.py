from django.urls import path
from . import views

urlpatterns = [
    path('', views.financie, name='financie'),
    path('simular/<int:veiculo_id>/', views.simular_financiamento, name='simular_financiamento'),
    path('sucesso/', views.financiamento_sucesso, name='financiamento_sucesso'),
]
