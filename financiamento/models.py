from django.db import models
from catalogo.models import Veiculo

class LeadFinanciamento(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name="leads")
    
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14)
    possui_cnh = models.BooleanField(default=False)
    valor_entrada = models.CharField(max_length=14)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.veiculo}"
