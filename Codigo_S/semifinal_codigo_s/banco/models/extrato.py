from django.db import models
from banco.models.cliente import Cliente
from banco.models.conta import Conta
from banco.models.movimentacao import Deposito, Saque, Transferencia


class Extrato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    extrato_conta = models.ManyToManyField(Conta)
    ultima_movimentacao = models.DateTimeField(auto_now=True)
    extrato_saque = models.ManyToManyField(Saque)
    extrato_deposito = models.ManyToManyField(Deposito)
    extrato_transferencia = models.ManyToManyField(Transferencia)

    def __str__(self):
        return f"Cliente: {str(self.cliente)}"

    def get_ultima_movimentacao(self):
        return self.ultima_movimentacao.strftime("%d/%m/%Y %H:%M")
