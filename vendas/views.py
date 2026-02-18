from django.shortcuts import render, redirect
from .forms import LeadVendaForm, UploadImagensForm
from .models import ImagemVenda

def enviar_veiculo(request):
    if request.method == 'POST':
        form_lead = LeadVendaForm(request.POST)
        
        # Aqui está o truque: validamos o formulário principal
        if form_lead.is_valid():
            lead = form_lead.save()

            # Em vez de validar o form_imagens, pegamos direto do request.FILES
            imagens = request.FILES.getlist('imagens') # 'imagens' deve ser o name do campo no seu HTML
            
            for img in imagens:
                ImagemVenda.objects.create(lead=lead, imagem=img)

            return redirect('venda_sucesso')
        else:
            print(f"Erros do Lead: {form_lead.errors}") # Debug caso o erro seja no texto
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