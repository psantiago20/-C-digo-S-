"""Exercício 4:

Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionário. Exemplo: dada o dicionário
>>> {1: “vermelho”, 2: “azul”, 3: “marrom”}
A saída deverá ser
>>> {1: 8, 2: 4, 3: 6}
"""

dic = {1: 'vermelho', 2: 'azul', 3: 'marrom'}
dic_2 = {}

for k,v in dic.items():
    dic_2[k] = len(v)

print(dic_2)
#Resolução @lilicostaro