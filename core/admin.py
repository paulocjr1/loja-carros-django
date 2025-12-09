from django.contrib import admin
from catalogo.models import Veiculo, VeiculoImagem

class VeiculoImagemInline(admin.TabularInline):
    model = VeiculoImagem
    extra = 1
    max_num = 8

# Registre o Veiculo APENAS AQUI, incluindo todas as configurações de listagem e o inline.
@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    # Adicione as configurações de listagem que estavam em core/admin.py
    list_display = ('marca', 'modelo', 'ano', 'cor', 'tipo_combustivel', 'preco')
    list_filter = ('marca', 'tipo_combustivel', 'ano')
    search_fields = ('marca', 'modelo')
    
    # Adicione o Inline para as imagens
    inlines = [VeiculoImagemInline]