from django.shortcuts import render
from catalogo.models import Veiculo

def home(request): 
    veiculos = Veiculo.objects.all().order_by('-ano') 
  
    context = {
        'veiculos': veiculos # Chave 'veiculos' para o template
    }
    
    # Renderiza o template correto (usando o nome que você mencionou anteriormente)
    return render(request, 'core/home.html', context)