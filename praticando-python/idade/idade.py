from random import randint, sample
from time import sleep

print('\033[33m-=\033[m' * 20)
print(f'\033[4;34m{"ACERTE O NÚMERO":-^40}\033[m')
print('\033[33m-=\033[m' * 20)

user = input('QUAL É O SEU NOME? ').strip()
print('-' * 40)

print('''DEFINA A QUANTIDADE DE NÚMEROS:
            \033[32m[ 1 ] 1 NÚMERO\033[m
            \033[33m[ 2 ] 3 NÚMEROS\033[m
            \033[35m[ 3 ] 5 NÚMEROS\033[m
            \033[31m[ 4 ] SAIR\033[m''')
quantidade = int(input('DEFINA AQUI A QUANTIDADE: '))
print('-' * 40)

print('REGRAS...')
print('OS NÚMEROS SÃO SORTEADOS DO 1 ATÉ O 60!')
print('-' * 40)

if quantidade in [1, 2, 3]:
    if quantidade == 1:
        num_escolhidos = [int(input('\033[34mESCOLHA O SEU NÚMERO: \033[m'))]
        sorteados = sample(range(1, 61), 1)
    elif quantidade == 2:
        num_escolhidos = [int(input(f'\033[34mESCOLHA O SEU ({i + 1}) NÚMERO: \033[m')) for i in range(3)]
        sorteados = sample(range(1, 61), 3)
    elif quantidade == 3:
        num_escolhidos = [int(input(f'ESCOLHA O SEU ({i + 1}) NÚMERO: ')) for i in range(5)]
        sorteados = sample(range(1, 61), 5)

    print('SORTEANDO NÚMEROS...')
    sleep(3)
    
    print('-' * 40)
    print(f'\033[34mSEUS NÚMEROS: {num_escolhidos}\033[m')
    print(f'\033[33mNÚMEROS SORTEADOS: {sorteados}\033[m')
    print('-' * 40)

    # Verificação se algum número do usuário está nos números sorteados
    acertos = set(num_escolhidos) & set(sorteados)
    if acertos:
        print(f'\033[32m{user}, VOCÊ ACERTOU OS SEGUINTES NÚMEROS: {list(acertos)}!\033[m')
    else:
        print(f'\033[31m{user}, NÃO FOI DESSA VEZ!\033[m')
        
elif quantidade == 4:
    print('FIM')
else:
    print('OPÇÃO INVÁLIDA!')
