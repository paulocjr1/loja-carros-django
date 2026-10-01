from django.shortcuts import render, redirect
from .forms import LeadVendaForm, UploadImagensForm
from .models import ImagemVenda

def enviar_veiculo(request):
    if request.method == 'POST':
        form_lead = LeadVendaForm(request.POST)
        form_imagens = UploadImagensForm(request.POST, request.FILES)
        
        # Validamos os dados do veículo e salvamos as fotos enviadas.
        if form_lead.is_valid():
            lead = form_lead.save()

            imagens = request.FILES.getlist('imagens')
            
            for img in imagens:
                ImagemVenda.objects.create(lead=lead, imagem=img)

            return redirect('venda_sucesso')

    else:
        form_lead = LeadVendaForm()
        form_imagens = UploadImagensForm()

    return render(request, 'vendas/form.html', {
        'form_lead': form_lead,
        'form_imagens': form_imagens
    })

# No final do arquivo vendas/views.py

def venda_sucesso(request):
    return render(request, 'vendas/sucesso.html')