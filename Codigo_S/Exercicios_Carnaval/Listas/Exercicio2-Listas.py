
"""Exercício 2:

Crie uma lista com 10 elementos (você escolhe quais serão) e imprima a lista na ordem inversa.
Exemplo: para a lista [1, 3, 6, “H”, [7,7,7] a saída deve ser
>>> [[7,7,7], “H”, 6, 3, 1]
"""

lista1 = [1,3,6,"H"]
lista2 = [7,7,7]
lista1.append(lista2)
novalista = lista1[::-1]

print(novalista)