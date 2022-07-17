"""Exercício 3:
Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem ser realocadas
para formar a outra palavra. Dada uma string qualquer, desenvolva um algoritmo que encontre o número de pares
de substrings que são anagramas.
"""
def anagramas(palavra):
    if len(palavra) <=1:
        return palavra
    else:
        tmp = []
        for aux in anagramas(palavra[1:]):
            for i in range(len(palavra)):
                tmp.append(aux[:i] + palavra[0:1] + aux[i:])
        return tmp
print(anagramas('abc'))