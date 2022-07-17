"""Exercício 7:

Dada a lista de strings [“1”, “7”, “99”, “15”] construa um programa que converte todos os elementos desta lista para inteiro.

Faça também o inverso, dada a mesma lista só que agora de elementos inteiros, converta todos os elementos para int.
"""
lista = ["1","7","99","15"]

print(f"Lista Original: {lista}")

lista_int = list(map(int, lista))

print(f"Lista em Inteiro: {lista_int}")

lista_str = list(map(str, lista_int))

print(f"Lista de volta a Str: {lista_str}")