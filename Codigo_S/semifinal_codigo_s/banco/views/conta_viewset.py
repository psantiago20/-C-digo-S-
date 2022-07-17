from rest_framework import viewsets
from banco.models.conta import Conta
from banco.serializers.conta_serializer import ContaSerializer
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name="dispatch")
class ContaViewSet(viewsets.ModelViewSet):

    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
