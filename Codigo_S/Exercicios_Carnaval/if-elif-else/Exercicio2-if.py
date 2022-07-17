"""Exercício 2:

Escreva um programa que receba dois números e imprima na tela se o primeiro é divisível pelo segundo.
"""
primeiro = int(input("Digite o primeiro número: "))
segundo = int(input(" Digite o segundo número: "))

if primeiro % segundo:
    print("Não é divisível")
else:
    print("É divisivel")