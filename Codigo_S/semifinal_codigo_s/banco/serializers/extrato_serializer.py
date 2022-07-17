from rest_framework import serializers
from banco.models.extrato import Extrato


class ExtratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extrato
        fields = [
            "id",
            "cliente",
            "extrato_conta",
            "extrato_saque",
            "extrato_deposito",
            "extrato_transferencia",
            "get_ultima_movimentacao",
        ]
