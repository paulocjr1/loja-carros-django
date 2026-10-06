from django.shortcuts import render, get_object_or_404
from catalogo.models import Veiculo


def financie(request):
    veiculo_id = request.GET.get('veiculo')
    veiculo = get_object_or_404(Veiculo, pk=veiculo_id) if veiculo_id else None
    return render(request, 'financiamento/solicitar.html', {'veiculo': veiculo})
