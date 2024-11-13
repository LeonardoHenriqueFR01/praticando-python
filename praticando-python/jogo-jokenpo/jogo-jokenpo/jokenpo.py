# JOGO JOKENPO CRIADO POR Leonardo Henrique

from random import randint
from time import sleep

print('\033[0;33m-=\033[m' * 15)
print('\033[0;36m-----------JOKENPOO-----------\033[m')
print('\033[0;33m-=\033[m' * 15)

user = str(input('QUAL É O SEU NOME? '))
print(f'OLÁ {user} VAMOS JOGAR!')
print('-' * 30)
print('''\033[0;34m[ 1 ] PEDRA\033[m
\033[0;34m[ 2 ] PAPEL\033[m
\033[0;34m[ 3 ] TESOURA\033[m''')
jogada = int(input(f'{user} SELECIONE A SUA JOGADA: '))
computador = randint(1, 3)
print('-' * 30)

print('\033[0;35mJO\033[m')
sleep(1)
print('\033[0;35mKEN\033[m')
sleep(1)
print('\033[0;35mPOO!!!\033[m')
print('-' * 30)

opções = {1: 'PEDRA', 2: 'PAPEL', 3:'TESOURA'}
print(f'\033[0;31mCOMPUTADOR JOGOU: {opções[computador]}!\033[m')
print(f'\033[0;32m{user} JOGOU: {opções[jogada]}!\033[m')
print('-' * 30)

if jogada == computador:
    print('\033[0;33mEMPATE\033[m')
elif (jogada == 1 and computador == 3) or (jogada == 2 and computador == 1) or (jogada == 3 and computador == 2):
    print(f'\033[0;32m{user} VOCÊ GANHOU!\033[m')
else:
    print('\033[0;31mCOMPUTADOR VENCEU!\033[m')
