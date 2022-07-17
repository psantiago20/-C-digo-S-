from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from banco.models.extrato import Extrato
from banco.serializers.extrato_serializer import ExtratoSerializer
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name="dispatch")
class ExtratoViewSet(viewsets.ModelViewSet):

    queryset = Extrato.objects.all()
    serializer_class = ExtratoSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = ["ultima_movimentacao"]
    ordering_fields = ["ultima_movimentacao"]
