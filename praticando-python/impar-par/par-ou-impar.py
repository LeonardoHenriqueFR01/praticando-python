from random import randint
from time import sleep

print('-=-' * 30)
print('IMPAR OU PAR')
print('-=-' * 30)

user = str(input('Qual é o seu nome? '))
print(f'Certo {user} vamos jogar!')
print('-' * 60)

num_sist = randint(1, 999999)
num_resp = num_sist % 2

print('PARA NÚMEROS IMPARES DIGITE: 1')
print('PARA NÚMEROS PARES DIGITE: 0')
print('-' * 70)

print('GERANDO O NÚMERO...')
sleep(10)
print('GERANDO O NÚMERO...')
sleep(5)

print('=' * 70)
print(f'O NÚMERO GERADO FOI: {num_sist}')
num_user = int(input(f'{user} o número e IMPAR ou PAR? '))
print('=' * 70)

if num_user == num_resp:
    print(f'{user} PARABÊNS VOCÊ ACERTOU!')
else:
    print(f'{user} VOCÊ ERROU!')

print('-=-' * 30)
print('APERTE F5 PARA TENTAR NOVAMENTE!')
print('-=-' * 30)
