# SORTEANDO ALUNOS desafio 019

from random import choice

aluno_1 = str(input('NOME DO PRIMEIRO ALUNO: '))
aluno_2 = str(input('NOME DO SEGUNDO ALUNO: '))
aluno_3 = str(input('NOME DO TERCEIRO ALUNO: '))
aluno_4 = str(input('NOME DO QUARTO ALUNO: '))

list_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
aluno_sort = choice(list_alunos)

print(f'O ALUNO QUE IRÁ APAGAR O QUADRO VAI SER O {aluno_sort}!')
