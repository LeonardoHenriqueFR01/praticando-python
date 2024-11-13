# TEST TABUADA V2 CRIADA POR Leonardo Henrique

from time import sleep

print('\033[0;33m-=\033[m' * 20)
print(f'\033[4;35m{"TABUADA V2":-^40}\033[m')
print('\033[0;33m-=\033[m' * 20)

print('''SELECIONE UMA DAS OPÇÕES
        [ 1 ] MULTIPLICAÇÃO
        [ 2 ] DIVISÃO
        [ 3 ] RAIZ-QUADRADA
        [ 4 ] TABUADA
        [ 5 ] SAIR''')
print('-' * 40)
opção = int(input('SELECIONE SUA OPÇÃO: '))

if opção == 1:
    print('MULTIPLICAÇÃO SELECIONADA!')
    print('''SELECIONE A OPÇÃO
          [ 1 ] MULTIPLICAR (2) NÚMEROS
          [ 2 ] MULTIPLICAR (3) NÚMEROS
          [ 3 ] MULTIPLICAR (4) NÚMEROS''')
    mul_opc = int(input('SELECIONE A OPÇÃO: '))
    if  mul_opc == 1:
        num_1 = int(input('SELECIONE O PRIMEIRO VALOR: '))
        num_2 = int(input('SELECIONE O SEGUNDO VALOR: '))
        print('GERANDO OPERAÇÃO...')
        sleep(3)
        print(f'{num_1} x {num_2} = {num_1 * num_2:.2f}')
    elif mul_opc == 2:
        num_1 = int(input('SELECIONE O PRIMEIRO VALOR: '))
        num_2 = int(input('SELECIONE O SEGUNDO VALOR: '))
        num_3 = int(input('SELECIONE O TERCEIRO VALOR: '))
        print('GERANDO OPERAÇÃO...')
        sleep(3)
        print(f'{num_1} x {num_2} x {num_3} = {num_1 * num_2 * num_3:.2f}')
    elif mul_opc == 3:
        num_1 = int(input('SELECIONE O PRIMEIRO NÚMERO: '))
        num_2 = int(input('SELECIONE O SEGUNDO NÚMERO: '))
        num_3 = int(input('SELCIONE O TERCEIRO NÚMERO: '))
        num_4 = int(input('SELECIONE O QUARTO VALOR: '))
        print('GERANDO OPERAÇÃO...')
        sleep(3)
        print(f'{num_1} x {num_2} x {num_3} x {num_4} = {num_1 * num_2 * num_3 * num_4:.2f}')
    else:
        print('OPÇÃO INVALIDA!')
elif opção == 2:
    print('DIVISÃO SELECIONADA!')
    print('''SELECIONE A OPÇÃO
          [ 1 ] DIVIDIR (2) NÚMEROS
          [ 2 ] DIVIDIR (3) NÚMEROS
          [ 3 ] DIVIDIR (4) NÚMEROS''')
    div_opc = int(input('SELECIONE A OPÇÃO: '))
    if div_opc == 1:
        num_1 = int(input('SELECIONE O PRIMEIRO VALOR: '))
        num_2 = int(input('SELECIONE O SEGUNDO VALOR: '))
        print('GERANDO OPERAÇÃO...')
        sleep(3)
        print(f'{num_1} / {num_2} = {num_1 / num_2:.2f}')
    elif div_opc == 2:
        num_1 = int(input('SELECIONE O PRIMEIRO VALOR: '))
        num_2 = int(input('SELECIONE O SEGUNDO VALOR: '))
        num_3 = int(input('SELECIONE O TERCEIRO VALOR: '))
        print('GERANDO OPERAÇÃO...')
        sleep(3)
        print(f'{num_1} / {num_2} / {num_3} = {num_1 / num_2 / num_3:.2f}')
    elif div_opc == 3:
        num_1 = int(input('SELECIONE O PRIMEIRO VALOR: '))
        num_2 = int(input('SELECIONE O SEGUNDO VALOR: '))
        num_3 = int(input('SELECIONE O TERCEIRO VALOR: '))
        num_4 = int(input('SELECIONE O QUARTO VALOR: '))
        print('GERANDO OPERAÇÃO...')
        sleep(3)
        print(f'{num_1} / {num_2} / {num_3} / {num_4} = {num_1 / num_2 / num_3 / num_3:.2f}')
    else:
        print('OPÇÃO INVALIDA!')
elif opção == 3:
    print('RAIZ-QUADRADA SELECIONADA!')
    num = int(input('SELECIONE O NÚMERO QUE VOCÊ DESEJA SABER A RAIZ-QUADRADA: '))
    print('GERANDO OPERAÇÃO...')
    sleep(3)
    print(f'A RAIZ-QUADRADA DE {num} É: {num ** 0.5:.2f}')
elif opção == 4:
    num_tab = int(input('DIGITE O NÚMERO QUE VOCÊ DESEJA VER A TABUADA: '))
    print('GERANDO OPERAÇÃO...')
    sleep(3)
    for tab in range(1, 11):
        print(f'{num_tab} x {tab} = {num_tab * tab:.2f}')
elif opção == 5:
    print('FIM!')

else:
    print('OPÇÃO INVALIDA!')
