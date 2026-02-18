from django.db import models

class LeadVenda(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    placa = models.CharField(max_length=14)
    veiculo_marca = models.CharField(max_length=100)
    veiculo_modelo = models.CharField(max_length=100)
    veiculo_ano = models.PositiveIntegerField()
    veiculo_km = models.PositiveIntegerField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.veiculo_marca} {self.veiculo_modelo}"


class ImagemVenda(models.Model):
    lead = models.ForeignKey(LeadVenda, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='uploads/veiculos/')