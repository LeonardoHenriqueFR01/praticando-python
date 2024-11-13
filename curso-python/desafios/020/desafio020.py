# SORTEANDO ALUNOS desafio 020


from random import shuffle
from time import sleep

print('-=' * 20)
print(f'{"SORTEANDO ALUNOS":-^40}')
print('-=' * 20)

aluno_1 = str(input('NOME DO PRIMEIRO ALUNO: '))
aluno_2 = str(input('NOME DO SEGUNDO ALUNO: '))
aluno_3 = str(input('NOME DO TERCEIRO ALUNO: '))
aluno_4 = str(input('NOME DO QUARTO ALUNO: '))
list_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(list_alunos)

print('VAMOS SORTEAR A ORDEM DE APRESENTAÇÃO DO TRABALHO!')
sleep(2)

ordem_formatada = ', '.join(list_alunos)
print(f'A ORDEM DE APRESENTAÇÃO SERA {ordem_formatada}!')
