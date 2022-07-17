from rest_framework import serializers
from banco.models.movimentacao import Deposito, Saque, Transferencia


class DepositoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposito
        fields = ["id", "conta", "valor", "get_data_deposito"]


class SaqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saque
        fields = ["id", "conta", "valor", "get_data_saque"]


class TransferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transferencia
        fields = ["id", "debito", "credito", "valor", "get_data_transferencia"]
