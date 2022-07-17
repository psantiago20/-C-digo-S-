"""Exercício 1:

Neste exercício, você criará um programa que calcula a média de uma coleção de valores inseridos pelo usuário e imprime-a na tela.
O usuário digitará 0 como um valor para indicar que nenhum outro valor será fornecido. Seu programa deve exibir uma mensagem de erro
se o primeiro valor inserido pelo usuário for 0.

Atenção!
Como o 0 é um valor de condição de parada, ele não deve entrar no cálculo da média!
"""

dados = []

while True:
   if 0 not in dados:
      dados.append(float(input("Digite uma nota para calcular a média. (0 para sair): ")))
   else:
      break

   nota_media = sum(dados) / len(dados)

   print(f"A média dos números é {nota_media}")