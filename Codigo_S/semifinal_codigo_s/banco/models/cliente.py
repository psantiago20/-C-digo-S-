from django.db import models
from banco.models.constants import CLIENTE_CHOICES, FISICA


class Cliente(models.Model):

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    tipo = models.CharField(max_length=2, choices=CLIENTE_CHOICES, default=FISICA)
    cpf = models.CharField(max_length=11, null=True, help_text="Somente números.")
    cnpj = models.CharField(max_length=14, null=True, help_text="Somente números.")
    cidade = models.CharField(max_length=256)
    cep = models.PositiveIntegerField(verbose_name="CEP")
    pais = models.CharField(max_length=256, verbose_name="País")

    def __str__(self) -> str:
        return self.nome
