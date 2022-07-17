
"""Exercício 3:

No exercício acima você calculou a área de um triângulo a partir da sua base e altura.
Faça um programa que receba os 3 lados de um triângulo – s1, s2 e s3 – e calcule sua área.
Compare a resposta com o exercício acima, dada das mesmas entradas. Os resultados devem ser idênticos.

"""
import math

s1 = float(input("Digite o tamanho do primeiro lado: "))
s2 = float(input("Digite o tamanho do segundo lado: "))
s3 = float(input("Digite o tamanho do terceiro lado: "))
s = (s1 + s2 + s3)/2

area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))

print(f"A área do triângulo é: {area:.2f}")