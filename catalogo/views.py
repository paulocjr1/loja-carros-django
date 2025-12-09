from django.shortcuts import render, get_object_or_404
from .models import Veiculo

def veiculo_detalhe(request, pk):
    # pega o veículo pelo id (pk)
    veiculo = get_object_or_404(Veiculo, pk=pk)
    
    # renderiza o template "carro.html"
    return render(request, 'catalogo/carro.html', {'veiculo': veiculo})