# MENU DE SOMAS desafio 059

from time import sleep

num_1 = int(input('PRIMEIRO VALOR: '))
num_2 = int(input('SEGUNDO VALOR: '))

opção = 0

while opção != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR''')
    opção = int(input('QUAL É A SUA OPÇÃO? '))
    
    if opção == 1:
        print(f'{num_1} + {num_2} = {num_1 + num_2}')
    
    elif opção == 2:
        print(f'{num_1} x {num_2} = {num_1 * num_2}')

    elif opção == 3:
        if num_1 > num_2:
            print(f'ENTRE {num_1} E {num_2} {num_1} É MAIOR!')
        elif num_1 == num_2:
            print(f'OS VALORES SÃO IGUAIS!')
        else:
            print(f'ENTRE {num_1} E {num_2} {num_2} É MAIOR!')
            
    elif opção == 4:
        print('INFORME OS NÚMEROS NOVAMENTE.')
        num_1 = int(input('PRIMEIRO VALOR: '))
        num_2 = int(input('SEGUNDO VALOR: '))

    elif opção == 5:
        print('FINALIZANDO...')

    else:
        print('OPÇÃO INVÀLIDA... TENTE NOVAMENTE.')


sleep(2)
print('FIM DO PROGRAMA!')
