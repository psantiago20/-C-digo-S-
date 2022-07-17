from rest_framework import viewsets, filters
from banco.models.cliente import Cliente
from banco.serializers.cliente_serializer import ClienteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name="dispatch")
class ClienteViewset(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = ["nome"]
    ordering_fields = ["nome"]
