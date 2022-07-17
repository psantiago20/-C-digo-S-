"""Exercício 3:

A tabela a seguir lista os níveis sonoros em decibéis para alguns barulhos comuns
Barulho	               Nível sonoro (dB)
Britadeira	                 130
Cortador de grama	         106
Despertador	                  70
Cômodo em silêncio	          40


Escreva um programa que leia um valor de nível sonoro do usuário em decibéis.
Se o valor for um dos que estão na tabela, o programa deve retornar aquele barulho.
Caso o número esteja entre algum dos valores da tabela, o programa deve dizer entre quais barulhos o valor digitado está.
Seu programa deve informar também quando o valor for menor que o ruído mínimo da tabela e maior que ruído máximo.
"""

db = int(input("Digite a quantidade de decibéis: "))

if db > 130:
    print("Barulho maior que de uma Britadeira")
    
elif db == 130:
    print("Barulho igual ao de uma Britadeira")

elif db > 106:
    print("Barulho entre o de um Cortador de Gramas (106db) e de uma Britadeira(130db)")

elif db == 106:
    print("Barulho igual ao de uma Cortador de Gramas")

elif db > 70:
    print("Barulho entre o de um Despertador(70db) e de um Cortador de Gramas (106db)")

elif db == 70:
    print("Barulho igual ao de um Despertador")

elif db > 40:
    print("Barulho entre o de um Cômodo em silêncio(40db) e de um Despertador (70db)")

elif db == 40:
    print("Barulho igual ao de um Cômodo em silêncio")

else:
    print("Barulho menor que de um Cômodo em silêncio")
