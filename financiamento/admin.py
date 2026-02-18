from django.contrib import admin
from .models import LeadFinanciamento

@admin.register(LeadFinanciamento)
class LeadFinanciamentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "telefone", "cpf", "possui_cnh", "veiculo", "criado_em")
    search_fields = ("nome", "telefone", "cpf")
    list_filter = ("possui_cnh", "criado_em")
