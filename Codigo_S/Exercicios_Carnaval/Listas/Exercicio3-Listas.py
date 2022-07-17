
"""Exercício 3:

Crie uma lista com 6 números inteiros. Imprima o maior, o menor e suas respectivas posições.
Exemplo: para a lista [5,4,6,8,3,4] a saída deve ser
>>> O maior elemento é 8 e está na posição 3
>>> O menor elemento é 3 e está na posição 4

Obs: caso o maior ou o menor número sejam repetidos, trazer a menor posição.
"""

lista = [5,4,6,8,3,4]
maior = max(lista)
menor = min(lista)
print(f"O maior elemento é {maior} e sua posição é {lista.index(maior)};\nO menor elemento é {menor} e sua posição é {lista.index(menor)}.")