from django.shortcuts import render
from catalogo.models import Veiculo
from django.db.models import Q
from django.http import JsonResponse
from core.currency import format_brl, parse_brl


def home(request):
    veiculos = Veiculo.objects.all().order_by('-ano', 'marca', 'modelo')
    q = request.GET.get('q', '').strip()
    if q:
        veiculos = veiculos.filter(Q(marca__icontains=q) | Q(modelo__icontains=q))

    total_veiculos = veiculos.count()
    context = {
        'veiculos': veiculos[:3],
        'total_veiculos': total_veiculos,
    }
    return render(request, 'core/home.html', context)


def page_not_found(request, exception=None, **kwargs):
    return render(request, '404.html', status=404)


def _get_int_param(request, key):
    raw = request.GET.get(key, '').strip()
    try:
        return int(raw) if raw else None
    except ValueError:
        return None


def estoque(request):
    queryset = Veiculo.objects.all().order_by('-ano', 'marca', 'modelo')
    q = request.GET.get('q', '').strip()
    marca = request.GET.get('marca', '').strip()
    cor = request.GET.get('cor', '').strip()
    cambio = request.GET.get('cambio', '').strip()
    combustivel = request.GET.get('combustivel', '').strip()

    if q:
        queryset = queryset.filter(Q(marca__icontains=q) | Q(modelo__icontains=q))
    if marca:
        queryset = queryset.filter(marca__iexact=marca)
    if cor:
        queryset = queryset.filter(cor__iexact=cor)
    if cambio:
        queryset = queryset.filter(cambio__iexact=cambio)
    if combustivel:
        queryset = queryset.filter(tipo_combustivel=combustivel)

    ano_de = _get_int_param(request, 'ano_de')
    ano_ate = _get_int_param(request, 'ano_ate')
    km_de = _get_int_param(request, 'km_de')
    km_ate = _get_int_param(request, 'km_ate')
    if ano_de is not None:
        queryset = queryset.filter(ano__gte=ano_de)
    if ano_ate is not None:
        queryset = queryset.filter(ano__lte=ano_ate)
    if km_de is not None:
        queryset = queryset.filter(quilometragem__gte=km_de)
    if km_ate is not None:
        queryset = queryset.filter(quilometragem__lte=km_ate)

    preco_de_text = request.GET.get('preco_de', '').strip()
    preco_ate_text = request.GET.get('preco_ate', '').strip()
    preco_de = parse_brl(preco_de_text)
    preco_ate = parse_brl(preco_ate_text)
    filtro_preco_invalido = bool((preco_de_text and preco_de is None) or (preco_ate_text and preco_ate is None))

    veiculos = list(queryset)
    if preco_de is not None or preco_ate is not None:
        filtrados = []
        for veiculo in veiculos:
            preco = parse_brl(veiculo.preco)
            if preco is None:
                continue
            if preco_de is not None and preco < preco_de:
                continue
            if preco_ate is not None and preco > preco_ate:
                continue
            filtrados.append(veiculo)
        veiculos = filtrados

    ordenacao = request.GET.get('ordenar', 'recentes')
    if ordenacao == 'preco_menor':
        veiculos.sort(key=lambda veiculo: (parse_brl(veiculo.preco) is None, parse_brl(veiculo.preco) or 0))
    elif ordenacao == 'preco_maior':
        veiculos.sort(key=lambda veiculo: (parse_brl(veiculo.preco) is None, -(parse_brl(veiculo.preco) or 0)))
    elif ordenacao == 'ano_antigo':
        veiculos.sort(key=lambda veiculo: (veiculo.ano, veiculo.pk))
    else:
        veiculos.sort(key=lambda veiculo: (-veiculo.ano, veiculo.pk))

    context = {
        'veiculos': veiculos,
        'total_veiculos': len(veiculos),
        'marcas': Veiculo.objects.order_by('marca').values_list('marca', flat=True).distinct(),
        'anos': Veiculo.objects.order_by('-ano').values_list('ano', flat=True).distinct(),
        'cores': Veiculo.objects.exclude(cor='').order_by('cor').values_list('cor', flat=True).distinct(),
        'cambios': Veiculo.objects.exclude(cambio__isnull=True).exclude(cambio='').order_by('cambio').values_list('cambio', flat=True).distinct(),
        'combustiveis': Veiculo.TIPOS_COMBUSTIVEL,
        'filtro_preco_invalido': filtro_preco_invalido,
    }
    return render(request, 'core/estoque.html', context)

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
                'preco': format_brl(v.preco),
                'img': img,
                'url': f"/veiculos/{v.id}/"
            })

    return JsonResponse(resultados, safe=False)
