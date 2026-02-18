from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from catalogo.models import Veiculo, VeiculoImagem
from .forms import VeiculoForm

# LISTAR
@login_required
def painel(request):
    veiculos = Veiculo.objects.all()
    return render(request, "painel/painel.html", {"veiculos": veiculos})


# CRIAR
@login_required
def criar_veiculo(request):
    if request.method == "POST":
        form = VeiculoForm(request.POST, request.FILES)

        if form.is_valid():
            veiculo = form.save()

            # múltiplas imagens
            imagens = request.FILES.getlist('imagens')
            for img in imagens:
                VeiculoImagem.objects.create(
                    veiculo=veiculo,
                    imagem=img
                )

            return redirect("painel")
    else:
        form = VeiculoForm()

    return render(request, "painel/form_veiculo.html", {"form": form})
# EDITAR
@login_required
def editar_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)

    if request.method == "POST":
        form = VeiculoForm(request.POST, request.FILES, instance=veiculo)

        if form.is_valid():
            veiculo = form.save()

            # novas imagens adicionadas
            imagens = request.FILES.getlist('imagens')
            for img in imagens:
                VeiculoImagem.objects.create(
                    veiculo=veiculo,
                    imagem=img
                )

            return redirect("painel")
    else:
        form = VeiculoForm(instance=veiculo)

    return render(request, "painel/form_veiculo.html", {
        "form": form,
        "veiculo": veiculo
        })


# DELETAR
@login_required
def deletar_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    veiculo.delete()
    return redirect("painel")
