from rest_framework import serializers
from banco.models.cliente import Cliente
from banco.validator.validator import valida_cnpj, valida_cpf


class ClienteSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(min_length=10, max_length=120)
    cnpj = serializers.CharField(required=False)
    cpf = serializers.CharField(required=False)

    class Meta:
        model = Cliente
        fields = "__all__"

    def validate_cpf(self, cpf):
        if valida_cpf(cpf):
            raise serializers.ValidationError({"CPF": "CPF deve ser numerico"})

        return cpf

    def validate_cnpj(self, cnpj):
        if not valida_cnpj(cnpj):
            raise serializers.ValidationError({"cnpj": "O CNPJ deve ter 14 dígitos"})

        return cnpj
