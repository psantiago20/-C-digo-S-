"""Desafio 1:

Implemente um jogo em que o usuário tenha que adivinhar um número sorteado pelo computador.

1.	O jogo deve sortear um número entre 1 e 100.
2.	O usuário deve informar um número. O número informado pelo usuário deve ser validado: não pode ser inferior a 1 ou superior a 100. Enquanto o usuário informar um número inválido, o jogo deve solicitar a entrada de um novo número.
3.	O número do usuário deve ser analisado:
a.	Caso o usuário informe um número inferior ao número sorteado, o jogo deve apresentar a mensagem “O número sorteado é maior.”.
b.	Caso o usuário informe um número superior ao número sorteado, o jogo deve apresentar a mensagem “O número sorteado é menor.”.
c.	Caso o usuário informe um número igual ao número sorteado, o jogo deve apresentar a mensagem “Parabéns! Você acertou o número sorteado”
e o jogo deve ser finalizado, sendo apresentado ao usuário a quantidade de tentativas efetuadas até este momento.
4.	Ao final do jogo, deve-se questionar o usuário se ele deseja jogar novamente. Caso afirmativo, todo o processo deve ser repetido. Caso contrário, o jogo deve ser encerrado.

Dica!
Pesquise sobre o módulo buit-in do Python chamado random
"""
import random
palpites = 0

while True:
    numeros = int(input("Digite um número de 1 a 100: "))
    n = random.randrange(1,101,1)
    palpites += 1
    print(n)
    
    if n < numeros:
        print(f"Você errou! O número sorteado é maior. Seu número: {numeros}, número sorteado: {n}")
    elif n > numeros:
        print(f"Você errou! O número sorteado é menor. Seu número: {numeros}, número sorteado: {n}")
    else:
        print(f"Parabéns! Você acertou o número sorteado em {palpites} tentativas. Seu número: {numeros}, número sorteado: {n}")
    continuar = (str(input("Deseja continuar? s/n: ").lower()))
    if continuar == "s":
        continue
    break