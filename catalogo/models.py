from django.db import models

class Veiculo(models.Model):
    TIPOS_COMBUSTIVEL = [
        ('GAS', 'Gasolina'),
        ('ETA', 'Etanol'),
        ('DIE', 'Diesel'),
        ('FLEX', 'Flex'),
        ('ELE', 'Elétrico'),
        ('HIB', 'Híbrido'),
    ]

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    cor = models.CharField(max_length=30)
    tipo_combustivel = models.CharField(max_length=5, choices=TIPOS_COMBUSTIVEL)
    portas = models.PositiveIntegerField(default=4)
    motor = models.CharField(max_length=20)  # ex: "1.0", "2.0 Turbo"
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='veiculos/imagens', blank=True, null=True)
    cambio = models.CharField(max_length=20, blank=True, null=True)  # ex: "Manual", "Automático"
    quilometragem = models.PositiveIntegerField(default=0)  # em km
    potencia = models.CharField(max_length=50, blank=True, null=True)  # ex: "150 cv"
    final_placa = models.CharField(max_length=1, blank=True, null=True)  # ex: "1", "2", ..., "0"
    unico_dono = models.BooleanField(default=False)

   
    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano}"


class VeiculoImagem(models.Model):
    # Relacionamento 1-para-MUITOS: Muitas imagens adicionais para um Veículo.
    veiculo = models.ForeignKey(
        Veiculo, 
        on_delete=models.CASCADE, 
        related_name="imagens_adicionais" # Mudei o nome para 'imagens_adicionais' para clareza
    )
    
    # Imagens adicionais
    # Sugestão de upload_to: 'carros/galeria'
    imagem = models.ImageField(upload_to='veiculos/imagens') 

    def __str__(self):
        return f"Imagem de {self.veiculo} (Adicional)"