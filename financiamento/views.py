from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from catalogo.models import Veiculo
from .forms import LeadFinanciamentoForm


def simular_financiamento(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, id=veiculo_id)

    print("==== VIEW CHAMADA ====")
    print("METHOD:", request.method)

    if request.method == 'POST':
        form = LeadFinanciamentoForm(request.POST)
        print("POST RECEBIDO")

        if form.is_valid():
            print("FORM VALIDOU")

            lead = form.save(commit=False)
            lead.veiculo = veiculo
            lead.save()

            print("LEAD SALVO")
            print("REDIRECIONANDO...")

            return redirect('financiamento_sucesso')
        else:
            print("FORM INVALIDO:", form.errors)

    else:
        form = LeadFinanciamentoForm()
        print("GET REQUEST")

    return render(request, 'financiamento/form.html', {
        'form': form,
        'veiculo': veiculo
    })



def financiamento_sucesso(request):
    return render(request, 'financiamento/sucesso.html')
