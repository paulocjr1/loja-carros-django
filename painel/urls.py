from django.urls import path
from . import views

urlpatterns = [
    path("", views.painel, name="painel"),
    path("novo/", views.criar_veiculo, name="criar_veiculo"),
    path("editar/<int:id>/", views.editar_veiculo, name="editar_veiculo"),
    path("deletar/<int:id>/", views.deletar_veiculo, name="deletar_veiculo"),
    path('leads/', views.lista_leads, name='lista_leads'),
    path('painel/leads/<int:id>/', views.detalhe_lead, name='detalhe_lead'),
    path('vendas/', views.lead_vendas, name='lead_vendas'),
    path('painel/vendas/<int:id>/', views.detalhe_venda, name='detalhe_venda')
]