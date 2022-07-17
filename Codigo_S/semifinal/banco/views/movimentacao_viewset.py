from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from banco.models.movimentacao import Deposito, Saque, Transferencia
from banco.serializers.movimentacao_serializer import (
    DepositoSerializer,
    SaqueSerializer,
    TransferenciaSerializer,
)
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name="dispatch")
class DepositoViewSet(viewsets.ModelViewSet):
    queryset = Deposito.objects.all()
    serializer_class = DepositoSerializer


@method_decorator(login_required, name="dispatch")
class SaqueViewSet(viewsets.ModelViewSet):
    queryset = Saque.objects.all()
    serializer_class = SaqueSerializer


@method_decorator(login_required, name="dispatch")
class TransferenciaViewSet(viewsets.ModelViewSet):
    queryset = Transferencia.objects.all()
    serializer_class = TransferenciaSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = ["nome"]
    ordering_fields = ["nome"]
