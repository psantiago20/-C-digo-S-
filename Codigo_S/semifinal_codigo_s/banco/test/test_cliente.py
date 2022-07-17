import json
from django.test import TestCase
from rest_framework.test import APIClient
from banco.models.cliente import Cliente
from rest_framework import status


class ClienteTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_cliente_nome_error(self):
        # dado
        cliente = {"nome": "josé"}
        # quando
        response = self.client.post("/cliente/", cliente, format="json")

        # então
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cliente_nome_error_message(self):
        # dado
        cliente = {
            "nome": "pedro",
            "cep": "99999999",
            "cidade": "Itapetininga",
            "pais": "Brasil",
            "telefone": "+5515999999999",
        }
        # quando
        response = self.client.post("/cliente/", cliente, format="json")

        # então
        self.assertEqual(
            json.loads(response.content),
            {"nome": ["Certifique-se de que este campo tenha mais de 10 caracteres."]},
        )

    def test_cliente_post_sucesso(self):
        # dado
        cliente = {
            "nome": "Pedro Santiago",
            "cep": "99999999",
            "cidade": "Itapetininga",
            "pais": "Brasil",
            "telefone": "+5515999999999",
        }
        # quando
        response = self.client.post("/cliente/", cliente, format="json")

        # então
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_cliente_create(self):
        # dado
        Cliente.objects.create(
            nome="Pedro Santiago",
            cep="99999999",
            cidade="Itapetininga",
            pais="Brasil",
            telefone="+5515999999999",
        )

        # quando
        cliente = Cliente.objects.get(
            nome="Pedro Santiago",
            cep="99999999",
            cidade="Itapetininga",
            pais="Brasil",
            telefone="+5515999999999",
        )

        # então
        self.assertEqual(cliente.nome, "Pedro Santiago")
