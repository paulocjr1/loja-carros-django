from django.shortcuts import render
from catalogo.models import Veiculo
from django.db.models import Q
from django.http import JsonResponse


def home(request): 
    veiculos = Veiculo.objects.all().order_by('-ano')

    # filtros
    q = request.GET.get('q')
    marca = request.GET.get('marca')
    ano = request.GET.get('ano')
    km = request.GET.get('km')
    preco = request.GET.get('preco')
    cor = request.GET.get('cor')
    tipo = request.GET.get('tipo')

    if q:
        veiculos = veiculos.filter(
            Q(marca__icontains=q) |
            Q(modelo__icontains=q)
        )

    if marca:
        veiculos = veiculos.filter(marca__iexact=marca)

    if cor:
        veiculos = veiculos.filter(cor__iexact=cor)

    if ano:
        ano_min, ano_max = ano.split('-')
        veiculos = veiculos.filter(ano__gte=ano_min, ano__lte=ano_max)

    if km:
        km_min, km_max = km.split('-')
        veiculos = veiculos.filter(km_rodados__gte=km_min, km_rodados__lte=km_max)

    if preco:
        preco_min, preco_max = preco.split('-')
        veiculos = veiculos.filter(preco__gte=preco_min, preco__lte=preco_max)

    if tipo:
        if tipo == 'novo':
            veiculos = veiculos.filter(km_rodados__lt=1000)
        elif tipo == 'seminovo':
            veiculos = veiculos.filter(km_rodados__gte=1000)

    marcas = Veiculo.objects.values_list('marca', flat=True).distinct()

    context = {
        'veiculos': veiculos,
        'marcas': marcas
    }
    
    return render(request, 'core/home.html', context)



def quick_search(request):
    q = request.GET.get('q', '').strip()
    resultados = []

    if q:
        veiculos = Veiculo.objects.filter(
            Q(marca__icontains=q) |
            Q(modelo__icontains=q)
        )[:8]

        for v in veiculos:

            # imagem principal
            if v.imagem:
                img = v.imagem.url
            elif v.imagens_adicionais.first():
                img = v.imagens_adicionais.first().imagem.url
            else:
                img = '/static/img/sem-imagem.png'

            resultados.append({
                'id': v.id,
                'label': f"{v.marca} {v.modelo}",
                'ano': v.ano,
                'preco': str(v.preco),
                'img': img,
                'url': f"/veiculos/{v.id}/"
            })

    return JsonResponse(resultados, safe=False)