"""Exercício 3:

Faça um programa que ordene um dicionário por seus valores. Exemplo: dado o dicionário
>>> {“matemática”: 81, “física”: 83, “química”: 87} 
a saída deve ser 
>>> {“química”: 87, “física”: 83, matemática”: 81}
"""

materias = {'matemática': 81, 'física': 83, 'química': 87}
sorted_list = sorted(materias.items(), key=lambda x: x[1], reverse=True)
sorted_materias = dict(sorted_list)

print(sorted_materias)

#Resolução por PedroHPC