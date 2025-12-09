from django.shortcuts import render
from catalogo.models import Veiculo

# RECOMENDADO: Use esta função para a Home Page
def home(request): 
    
    # 1. Busca os veículos no banco de dados
    veiculos = Veiculo.objects.all().order_by('-ano') 
    
    # 2. Comando de debug (opcional, remova depois)
    # Ele deve estar FORA da definição do dicionário 'context'
    print(f"Número de veículos encontrados: {veiculos.count()}") 
    
    # 3. Adiciona a lista de veículos ao contexto do template
    context = {
        'veiculos': veiculos # Chave 'veiculos' para o template
    }
    
    # 4. Renderiza o template correto (usando o nome que você mencionou anteriormente)
    return render(request, 'core/home.html', context)


# A função 'home' abaixo é redundante e não passa dados; você pode excluí-la
# se a 'home_page' for a sua Home Page oficial.
# def home(request):
#     return render(request, 'core/home.html')