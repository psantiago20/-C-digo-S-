
"""
Escreva um programa que leia do usuário um número de 4 dígitos e imprima a soma destes dígitos.
Exemplo, se o usuário digitar 3141 seu programa deverá imprimir na tela 3+1+4+1=9.
"""
while True:
    lista = input("Digite 4 números inteiros: ")
    if len(lista) != 4 :
        print("Você deve digitar 4 números!")
        continue
    break
print(sum(int(i) for i in lista))