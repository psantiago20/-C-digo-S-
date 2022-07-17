"""Exercício 1:

Crie uma variável do tipo lista com 5 elementos (você escolhe quais serão).
Imprima na tela o elemento e sua respectiva posição na lista. Exemplo: para a lista [1, 3, 6, “H”, [7,7,7]] a saída deve ser:
>>> Elemento 1 na posição 0
>>> Elemento 3 na posição 1
>>> Elemento 6 na posição 2
>>> Elemento “H” na posição 3
"""

lista1 = [1,3,6,"H"]
lista2 = [7,7,7]
lista1.append(lista2)
print(f"Elemento {lista1[0]} na posição 0\nElemento {lista1[1]} na posição 1\nElemento {lista1[2]} na posição 2\nElemento {lista1[3]} na posição 3")