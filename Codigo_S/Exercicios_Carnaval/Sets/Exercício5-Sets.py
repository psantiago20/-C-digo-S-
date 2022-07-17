"""Exercício 5:

Faça um programa que encontre as notas mínimas e máximas de um dicionário, e imprima-os na tela com as suas respectivas chaves. Exemplo: dado o dicionário
>>> {“Theodoro”: 20, “Márcia”: 50, “Júnior”: 80}
A saída deve ser
>>> Nota máxima -> Júnior : 80
>>> Nota mínima -> Theodoro : 20

"""

dic = {"Theodoro": 20, "Márcia": 50, "Júnior": 80}
val = list(dic.values())
val.sort
max1 = max(val)
min1 = min(val)

minimo = min(dic, key=dic.get)
maximo = max(dic, key=dic.get)
print(f"Nota máxima -> {maximo} : {max1}\nNota mínima -> {minimo} : {min1}")