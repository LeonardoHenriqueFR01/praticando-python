# LOTERIA V2 CRIADO POR Leonardo Henrique

from random import randint
from time import sleep

print('\033[0;33m-=\033[m' * 20)
print(f'\033[4;32m{"LOTERIA V2":-^40}\033[m')
print('\033[0;33m-=\033[m' * 20)

print(f'\033[4;36m{"REGRAS":-^40}\033[m')
print('\033[4;32mVOCê DEVE ACERTAR 3 NÚMEROS PARA PODER \nGANHAR!\033[m')
print('-' * 40)

print('''FICHAS LIBERADAS
            \033[0;34m[ 1 ] 2 FICHAS\033[m''')

print('-' * 40)
ficha = int(input('SELECIONE O NÚMERO DE ACORDO COM AS FICHAS: '))
user = str(input('QUAL É O SEU NOME: '))

print('-' * 40)
print(f'\033[0;35m{f"VAMOS JOGAR {user}":-^40}\033[m')
print('-' * 40)

if ficha == 1:
        print(f'\033[4;33m{"VOCE TEM 2 FICHAS!":-^40}\033[m')
        print('-' * 40)
        user_num_1 = int(input('SELECIONE O SEU PRIMEIRO NÚMERO: '))
        user_num_2 = int(input('SELECIONE O SEU SEGUNDO NÚMERO: '))
        user_num_3 = int(input('SELECIONE O SEU TERCEIRO NÚMERO: '))
        user_num_list = [user_num_1, user_num_2, user_num_3]
        print('-' * 40)

        computer_num_1 = randint(1, 5)
        computer_num_2 = randint(1, 5) 
        computer_num_3 = randint(1, 5)
        computer_num_list = [computer_num_1, computer_num_2, computer_num_3]

        print(f'SEUS NÚMEROS: {user_num_list}')
        print('GERANDO RESULTADO...')
        sleep(2)
        print(f'NÚMEROS SORTEADOS: {computer_num_list}')
        print('-' * 40)

        if user_num_list == computer_num_list:
            print(f'PARABÊNS VOCÊ GANHOU!')

        elif user_num_1 != computer_num_list:
            print(f'\033[4;33m{"VOCE TEM 1 FICHA!":-^40}\033[m')
            print('-' * 40)
            user_num_1 = int(input('SELECIONE O SEU PRIMEIRO NÚMERO: '))
            user_num_2 = int(input('SELECIONE O SEU SEGUNDO NÚMERO: '))
            user_num_3 = int(input('SELECIONE O SEU TERCEIRO NÚMERO: '))
            user_num_list = [user_num_1, user_num_2, user_num_3]
            print('-' * 40)

            computer_num_1 = randint(1, 5)
            computer_num_2 = randint(1, 5)
            computer_num_3 = randint(1, 5)
            computer_num_list = [computer_num_1, computer_num_2, computer_num_3]

            print(f'SEUS NÚMEROS: {user_num_list}')
            print('GERANDO RESULTADO...')
            sleep(2)
            print(f'NÚMEROS SORTEADOS: {computer_num_list}')
            print('-' * 40)
        else:
            print('VOCÊ PERDEU!')
            print('ACABOU AS SUAS FICHAS!') 
