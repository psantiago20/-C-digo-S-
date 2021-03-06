# Generated by Django 4.0.6 on 2022-07-17 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("telefone", models.CharField(max_length=14)),
                (
                    "tipo",
                    models.CharField(
                        choices=[("PF", "Fisica"), ("PJ", "Juridica")],
                        default="PF",
                        max_length=2,
                    ),
                ),
                (
                    "cpf",
                    models.CharField(
                        help_text="Somente números.", max_length=11, null=True
                    ),
                ),
                (
                    "cnpj",
                    models.CharField(
                        help_text="Somente números.", max_length=14, null=True
                    ),
                ),
                ("cidade", models.CharField(max_length=256)),
                ("cep", models.PositiveIntegerField(verbose_name="CEP")),
                ("pais", models.CharField(max_length=256, verbose_name="País")),
            ],
        ),
        migrations.CreateModel(
            name="Conta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "saldo",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=30,
                        verbose_name="Depósito Inicial",
                    ),
                ),
                (
                    "num_conta",
                    models.CharField(
                        default="",
                        editable=False,
                        max_length=6,
                        unique=True,
                        verbose_name="Número da conta",
                    ),
                ),
                (
                    "ultima_movimentacao",
                    models.DateTimeField(auto_now=True, verbose_name="Movimentação"),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="banco.cliente"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Deposito",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "valor",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("data_deposito", models.DateField(auto_now_add=True)),
                (
                    "conta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="banco.conta"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transferencia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "valor",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("data_transferencia", models.DateTimeField(auto_now_add=True)),
                (
                    "credito",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="credito",
                        to="banco.conta",
                        verbose_name="Conta creditada",
                    ),
                ),
                (
                    "debito",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="debito",
                        to="banco.conta",
                        verbose_name="Conta debitada",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Saque",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "valor",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("data_saque", models.DateTimeField(auto_now_add=True)),
                (
                    "conta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="banco.conta"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Extrato",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ultima_movimentacao", models.DateTimeField(auto_now=True)),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="banco.cliente"
                    ),
                ),
                ("extrato_conta", models.ManyToManyField(to="banco.conta")),
                ("extrato_deposito", models.ManyToManyField(to="banco.deposito")),
                ("extrato_saque", models.ManyToManyField(to="banco.saque")),
                (
                    "extrato_transferencia",
                    models.ManyToManyField(to="banco.transferencia"),
                ),
            ],
        ),
    ]
