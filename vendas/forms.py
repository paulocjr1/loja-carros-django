from django import forms
from .models import LeadVenda, ImagemVenda

# 1. Criamos um widget que explicitamente permite múltiplos arquivos
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class LeadVendaForm(forms.ModelForm):
    class Meta:
        model = LeadVenda
        fields = ['nome', 'telefone', 'placa', 'veiculo_marca', 'veiculo_modelo', 'veiculo_ano', 'veiculo_km', 'observacoes']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'veiculo_marca': forms.TextInput(attrs={'class': 'form-control'}),
            'veiculo_modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'veiculo_ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'veiculo_km': forms.NumberInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class UploadImagensForm(forms.Form):
    imagens = forms.FileField(
        widget=MultipleFileInput(attrs={'multiple': True, 'class': 'form-control'}),
        required=False  # Deixe False para testar se o formulário passa
    )