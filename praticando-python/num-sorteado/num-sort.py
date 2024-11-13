#ACERTE O NÚMERO SORTEADO DE 0 A 5

from random import randint
from time import sleep

print('-' * 40)
print('ACERTE O NÚMERO DE 0 A 5')
print('-' * 40)

user = str(input('Qual é o seu nome? '))
print(f'Ok {user} vamos jogar!')
print('ACERTE O NÚMERO DE 0 A 5')
print('-' * 40)

user_num = int(input('Digite o seu número: '))

print('-' * 40)
print(f'VOCÊ ESCOLHEU O NÚMERO: {user_num}')
num_ger = randint(0, 5)
print('GERANDO NÚMERO SORTEADO...')
sleep(10)

print(f'O NÚMERO GERADO FOI: {num_ger}')
print('-' * 40)

if user_num == num_ger:
    print(f'PARABÊNS {user} VOCÊ ACERTOU O NÚMERO SORTEADO!')
else:
    print(f'{user} NÃO FOI DESSA VEZ!')

print('-' * 30)
print('APERTE F5 PARA TENTAR NOVAMENTE')
print('-' * 30)
