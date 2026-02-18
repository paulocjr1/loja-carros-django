from django.contrib import admin
from .models import LeadVenda

@admin.register(LeadVenda)
class LeadVendaAdmin(admin.ModelAdmin):
    list_display = ("nome", "telefone", "placa", "veiculo_marca", "veiculo_modelo", "criado_em")
    search_fields = ("nome", "telefone", "cpf")