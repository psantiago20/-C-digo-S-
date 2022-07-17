from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from banco.models.conta import Conta


class Deposito(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    valor = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    data_deposito = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Valor depositado: +R${str(self.valor)} Data: {(self.data_deposito)}"

    def get_data_deposito(self):
        return self.data_deposito.strftime("%d/%m/%Y %H:%M")


@receiver(post_save, sender=Deposito)
def update_saldo(sender, instance, **kwargs):
    instance.conta.saldo += instance.valor
    instance.conta.save()


class Saque(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    valor = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    data_saque = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Valor retirado: -R${str(self.valor)} Data: {(self.data_saque)}"

    def get_data_saque(self):
        return self.data_saque.strftime("%d/%m/%Y %H:%M")


@receiver(post_save, sender=Saque)
def update_saldo(sender, instance, **kwargs):
    instance.conta.saldo -= instance.valor
    instance.conta.save()


class Transferencia(models.Model):
    debito = models.ForeignKey(
        Conta,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="debito",
        verbose_name="Conta debitada",
    )
    credito = models.ForeignKey(
        Conta,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="credito",
        verbose_name="Conta creditada",
    )
    valor = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    data_transferencia = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conta Debitada:{str(self.debito)} - R${str(self.valor)} ### Conta Creditada:{str(self.credito)} "

    def get_data_transferencia(self):
        return self.data_transferencia.strftime("%d/%m/%Y %H:%M")


@receiver(post_save, sender=Transferencia)
def update_saldo(sender, instance, **kwargs):
    instance.debito.saldo -= instance.valor
    instance.credito.saldo += instance.valor
    instance.debito.save()
    instance.credito.save()
