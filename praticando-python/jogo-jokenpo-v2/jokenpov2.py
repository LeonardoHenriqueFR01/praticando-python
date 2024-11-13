# JOGO JOKENPO V2 CRIADO POR Leonardo Henrique

from random import choice
from time import sleep

print('\033[0;33m-=\033[m' * 20)
print(f'\033[0;36m{"JOKENPOO(V2)":-^40}\033[m')
print('\033[0;33m-=\033[m' * 20)

user = str(input('QUAL É O SEU NOME? '))
print(f'OLÁ {user} VAMOS JOGAR!')
print('-' * 40)
opções = {1:'PEDRA', 2:'PAPEL', 3:'TESOURA'}

for cont in range(3):

    print('\033[0;34m          [ 1 ] PEDRA\033[m')
    print('\033[0;34m          [ 2 ] PAPEL\033[m')
    print('\033[0;34m          [ 3 ] TESOURA\033[m')
    print('-' * 40)

    jogada = int(input(f'{user} ESCOLHA A SUA JOGADA: '))
    if jogada != 1 and jogada != 2 and jogada != 3:
        print('-' * 40)
        print('\033[4;31mOPÇÃO INVÁLIDA! ESCOLHA 1, 2 OU 3.\033[m')
        print('-' * 40)
        jogada = int(input(f'{user} ESCOLHA A SUA JOGADA: '))

    comput = choice(list(opções.keys()))

    print('COMPUTADOR JOGANDO...')
    sleep(2)
    print('\033[0;35mJO\033[m')
    sleep(0.5)
    print('\033[0;35mKEN\033[m')
    sleep(0.5)
    print('\033[0;35mPO!!!\033[m')
    print('-' * 40)

    print(f'\033[4;32m{user} JOGOU: {opções[jogada]}\033[m')
    print(f'\033[4;31mCOMPUTADOR JOGOU: {opções[comput]}\033[m')
    print('-' * 40)

    if jogada == comput:
        print(f'\033[0;33m{"EMPATE!":-^40}\033[m')
        print('-' * 40)
    elif (jogada == 1 and comput == 3) or (jogada == 2 and comput == 1) or (jogada == 3 and comput == 2):
        print(f'\033[0;32m{"VOCÊ-VENCEU!":-^40}\033[m')
        print('-' * 40)
    else:
        print(f'\033[0;31m{"COMPUTADOR VENCEU!":-^40}\033[m')
        print('-' * 40)
