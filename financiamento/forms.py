from django import forms
from .models import LeadFinanciamento

class LeadFinanciamentoForm(forms.ModelForm):
    class Meta:
        model = LeadFinanciamento
        fields = ['nome', 'telefone', 'data_nascimento', 'cpf', 'possui_cnh', 'valor_entrada']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'possui_cnh': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'valor_entrada': forms.TextInput(attrs={'class': 'form-control'}),

        }
