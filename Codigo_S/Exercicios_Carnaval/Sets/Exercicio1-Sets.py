"""Exercício 1:

Digamos que existam 2 cursos de idiomas em uma escola, inglês e francês, e que existam alunos matriculados conforme abaixo:
•	Alunos matriculados em inglês:
o	João Alves dos Santos
o	Maria Magalhães
o	Antônio da Silva Ferreira
o	José Júnior Jarbas
o	Henrique da Silva Sauro
o	Joaquina Ferreira da Silva
o	Fabiana Aparecida Bianco
o	Marrone Gutierres
o	Carlos Magno Farad
o	Antônio da Silva Júnior Amaral

•	Alunos matriculados em francês:
o	João Alves dos Santos
o	Antônio da Silva Ferreira
o	Fernanda Abdala Mohamed
o	Abner Mignon Alib
o	Alisson Figueiredo
o	Henrique da Silva Sauro
o	Maria Magalhães
o	Marrone Gutierres
o	Joaquina Ferreira da Silva

Faça um programa que responda as seguintes perguntas:

1.	Quantos alunos estão matriculados na escola, no total?
2.	Quantos e quais estão matriculados APENAS em INGLES?
3.	Quantos e quais estão matriculados APENAS em FRANCES?
4.	Quantos e quais estão matriculados EM AMBOS os cursos?
5.	Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?

"""
#Resolução feita por @lilacostaro
escola = {'Alunos':[
              {'Aluno': [{'Nome': 'João Alves dos Santos', 'Cursos': ['inglês', 'francês']}]},
              {'Aluno': [{'Nome': 'Maria Magalhães', 'Cursos': ['inglês', 'francês']}]},
              {'Aluno': [{'Nome': 'Antônio da Silva Ferreira', 'Cursos': ['inglês', 'francês']}]},
              {'Aluno': [{'Nome': 'José Júnior Jarbas', 'Cursos': 'inglês'}]},
              {'Aluno': [{'Nome': 'Henrique da Silva Sauro', 'Cursos': ['inglês', 'francês']}]},
              {'Aluno': [{'Nome': 'Joaquina Ferreira da Silva', 'Cursos': ['inglês', 'francês']}]},
              {'Aluno': [{'Nome': 'Fabiana Aparecida Bianco', 'Cursos': 'inglês'}]},
              {'Aluno': [{'Nome': 'Marrone Gutierres', 'Cursos': ['inglês', 'francês']}]},
              {'Aluno': [{'Nome': 'Carlos Magno Farad', 'Cursos': 'inglês'}]},
              {'Aluno': [{'Nome': 'Antônio da Silva Júnior Amaral', 'Cursos': 'inglês'}]},
              {'Aluno': [{'Nome': 'Fernanda Abdala Mohamed', 'Cursos': 'francês'}]},
              {'Aluno': [{'Nome': 'Abner Mignon Alib', 'Cursos': 'francês'}]},
              {'Aluno': [{'Nome': 'Alisson Figueiredo', 'Cursos': 'francês'}]}
        ]}

    
qnt_alunos = len(escola['Alunos'])

ing_qnt = 0
alunos_ing = []
fran_qnt = 0
alunos_fran = []
all_qnt = 0
alunos_all = []

for i in range(qnt_alunos):
    
    nome = escola['Alunos'][i]['Aluno'][0]['Nome']
    curso = escola['Alunos'][i]['Aluno'][0]['Cursos']
    
    if curso == 'inglês':
        ing_qnt += 1 
        alunos_ing.append(nome)
    elif curso == 'francês':
        fran_qnt += 1 
        alunos_fran.append(nome)
    else:
        all_qnt += 1 
        alunos_all.append(nome)



# Resposta 1
print(f'\nQuantos alunos estão matriculados na escola, no total?\n{qnt_alunos}')

# Resposta 2
print(f'\nQuantos e quais estão matriculados APENAS em INGLES?\n{ing_qnt}\n\nEles são:\n')
for aluno in alunos_ing:
    print(aluno)

# Resposta 3
print(f'\nQuantos e quais estão matriculados APENAS em FRANCES?\n{fran_qnt}\n\nEles são:\n')
for aluno in alunos_fran:
    print(aluno)

# Resposta 4
print(f'\nQuantos e quais estão matriculados EM AMBOS os cursos?\n{all_qnt}\n\nEles são:\n')
for aluno in alunos_all:
    print(aluno)

# Resposta 5
print(f'\nQuantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?')
print(ing_qnt + fran_qnt)