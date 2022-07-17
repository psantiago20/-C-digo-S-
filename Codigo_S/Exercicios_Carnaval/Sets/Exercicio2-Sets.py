"""Exercício 2:

Faça um programa que lê uma sigla de um estado do usuário e imprime na tela o nome completo do estado. Exemplo:

>>> Digite um estado: SP
>>> O nome completo do estado é São Paulo.
"""

estados = {'AC': 'Acre', 'AL': 'Alagoas', 'AP': 'Amapá', 'AM': 'Amazonas','BA': 'Bahia','CE': 'Ceará','DF': 'Distrito Federal',
'ES': 'Espírito Santo', 'GO': 'Goiás', 'MA': 'Maranhão', 'MT': 'Mato Grosso', 'MS': 'Mato Grosso do Sul', 'MG': 'Minas Gerais',
'PA': 'Pará', 'PB': 'Paraíba', 'PR': 'Paraná', 'PE': 'Pernambuco','PI': 'Piauí', 'RJ': 'Rio de Janeiro', 'RN': 'Rio Grande do Norte',
'RS': 'Rio Grande do Sul', 'RO': 'Rondônia', 'RR': 'Roraima', 'SC': 'Santa Catarina', 'SP': 'São Paulo', 'SE': 'Sergipe',
'TO': 'Tocantins'}

est = input("Digite a sigla do estado: ").upper()

if est in estados.keys():
    print(f"Você está procurando por {est}: {estados[est]}")
else:
    print("Sigla não corresponde a um estado brasileiro")
