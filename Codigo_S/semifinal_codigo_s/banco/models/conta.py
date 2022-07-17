import random
from django.db import models
from banco.models.cliente import Cliente


class Conta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    agencia = "0001"
    saldo = models.DecimalField(
        verbose_name="Depósito Inicial", decimal_places=2, max_digits=30, default=0.00
    )
    num_conta = models.CharField(
        verbose_name="Número da conta",
        max_length=6,
        default="",
        editable=False,
        unique=True,
    )
    ultima_movimentacao = models.DateTimeField(
        auto_now=True, verbose_name="Movimentação"
    )

    def save(self, *args, **kwargs):

        random.seed = self.id
        self.num_conta = str(random.randint(1, 999999)).zfill(6)
        super().save()

    def __str__(self):
        return f"Conta: {str(self.num_conta)} ### Saldo: R${str(self.saldo)} Data: {(self.ultima_movimentacao)}"

    def get_ultima_movimentacao(self):
        return self.ultima_movimentacao.strftime("%d/%m/%Y %H:%M")
