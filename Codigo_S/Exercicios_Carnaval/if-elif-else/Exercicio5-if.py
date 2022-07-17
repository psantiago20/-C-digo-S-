"""Exercício 5:

Escreva um programa que receba uma string e diga se ela tem o formato de uma placa veicular brasileira (no formato antigo)
com três letras, um traço e quatro números. Exemplos: 
•	Dada a entrada ABT-1234 o programa deveria exibir True
•	Dada a entrada JKL9999 o programa deveria exibir False
•	Qualquer outra entrada que fuja do padrão de 3 letras, um traço e quatro números, o programa deverá exibir False 
"""
print("Verificação de placa do modelo antigo")

placa = input("Informe a placa do veículo:").upper()

if len(placa) != 8:
    placa_valida = False

else:
    letras = placa[:3]
    numeros = placa[-4:]
    traco = placa[3]

    if (letras.isalpha() and numeros.isdigit and traco == "-"):
        placa_valida = True
    else:
        placa_valida = False

print(f"A placa {placa} é válida? Resp: {placa_valida}")