# ACERTE OS 3 NÚMEROS DA LETERIA

from random import randint
from time import sleep

print('-' * 30)
print('ACERTE OS 3 NÚMEROS DA LOTERIA')
print('REGRAS: VOCÊ DEVE ESCOLHER 3 NÚMEROS DE 5 ATÉ 10')
print('-' * 30)

print('VAMOS COMEÇAR!')
user = str(input('Qual é o seu nome? '))
print(f'OK {user} VAMOS JOGAR!')
print('DIGITE SEUS 3 NÚMEROS')

num_user_1 = int(input('Digite seu primeiro número: '))
num_user_2 = int(input('Digite seu segundo número: '))
num_user_3 = int(input('Digite seu terceiro número: '))
print('-' * 30)
print('OK ESSES SÃO SEUS NÚMEROS!')
user_num_list = [num_user_1, num_user_2, num_user_3]
print(f'{user_num_list}')

num_sort_1 = randint(5, 10)
num_sort_2 = randint(5, 10)
num_sort_3 = randint(5, 10)
num_sort_list = [num_sort_1, num_sort_2, num_sort_3]

print('GERANDO NÚMEROS SORTEADOS...')
sleep(10)
print('NÚMEROS GERADO!')
print('VERIFICANDO RESULTADO...')
sleep(5)
print('=' * 30)
print('VEJA O RESULTADO!')
print(f'SEUS NÚMEROS: {user_num_list}')
print(f'NÚMEROS SORTEADOS: {num_sort_list}')
if user_num_list == num_sort_list:
    print(f'{user} VOCÊ GANHOU!')
else:
    print(f'{user} NÃO FOI DESSA VEZ!')
print('=' * 30)
print('APERTE F5 PARA TENTAR NOVAMENTE')
print('=' * 30)

