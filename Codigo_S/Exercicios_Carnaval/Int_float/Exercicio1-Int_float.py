"""Exercício 1:

Faça um programa que receba dois números inteiros do usuário, A e B e imprima na tela as seguintes operações:
•	A soma de A e B;
•	A diferença quando se subtrai B de A;
•	O produto (multiplicação) entre A e B;
•	O quociente (parte inteira da divisão) quando se divide A por B;
•	O resto da divisão entre A e B;
•	O resultado de log10 de A;
•	O resultado de A elevado a B;
"""

from math import log10

A = int(input("Digite um número inteiro: "))
B = int(input("Digite um segundo número inteiro: "))
soma = A + B
subtracao = A - B
Mult = A * B
Div = A / B
Rest = A % B
logA = log10(A)
Expo = A ** B

print(f"A soma é: {soma};\n A subtração é: {subtracao};\nA multiplicação é: {Mult};\nA divisão é: {Div:.2f};\nO resto da divisão é: {Rest:.2f}\nO log de A é: {logA}\nA exponenciação é: {Expo}")