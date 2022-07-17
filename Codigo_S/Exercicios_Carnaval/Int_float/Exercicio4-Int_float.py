
"""Exercício 4:

Faça um programa que receba do usuário seu peso em kg e altura em metros e imprima o Índice de Massa Corporal (IMC) do usuário.
"""

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)

if imc > 30:
    status = "Obesidade"
elif imc >=24.9:
    status = "Sobrepeso"
elif imc >= 18.5:
    status = "Normal"
else:
    status = "Magreza"

print(f"Seu IMC é de {imc:.2f}kg/m². De acordo com a Organização Mundial da Saúde seu IMC é de {status}.")
