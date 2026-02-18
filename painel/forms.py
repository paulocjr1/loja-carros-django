from django import forms
from catalogo.models import Veiculo, VeiculoImagem

class VeiculoForm(forms.ModelForm):
     class Meta:
        model = Veiculo
        fields = "__all__"

        widgets = {
            "preco": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ex: 85000"
            }),
            "construcao": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Ex: 2022"
            }),
            "descricao": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Descrição do veículo"
            }),
            "marca": forms.TextInput(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "ano": forms.NumberInput(attrs={"class": "form-control"}),
            "km_rodados": forms.NumberInput(attrs={"class": "form-control"}),
            "imagem": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


class VeiculoImagemForm(forms.ModelForm):
    class Meta:
        model = VeiculoImagem
        fields = ["imagem"]
