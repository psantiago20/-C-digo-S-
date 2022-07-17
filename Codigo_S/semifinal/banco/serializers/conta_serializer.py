from rest_framework import serializers
from banco.models.conta import Conta


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ["cliente", "agencia", "num_conta", "saldo", "get_ultima_movimentacao"]
