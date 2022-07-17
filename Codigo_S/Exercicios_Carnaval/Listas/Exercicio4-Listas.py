"""Exercício 4:

Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Em seguida, calcule a média anual das temperaturas e mostre a média calculada,
juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso):
Exemplo de saída:
>>> Meses com temperatura acima da média anual de 35,5°:
>>> 1 – janeiro
>>> 3 – março
>>> 6 – junho
"""
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperatura = []

for m in range(0, len(meses)):
    temperatura.append(float(input(f"Digite a temperatura do mês de {meses[m]}:")))

media = sum(temperatura)/len(temperatura)

for m in range(0, len(temperatura)):
    if temperatura[m] > media:
        print (str(f"{m+1} - {meses[m]} - {temperatura[m]}ºC"))
