# FUNÇÃO DE TODOOS OS OPERADORES CRIADO POR Leonado Henrique


print('-=' * 20)
print(f'\033[7;35{"OPERADORES":-^40}\033[m')
print('-=' * 20)

print('''TODOS OS OPERADORES
        [ 1 ] * (MULTIPLICAÇÃO)
        [ 2 ] / (DIVISÃO)
        [ 3 ] ** (POTÊNCIA)
        [ 4 ] % (DIVISÃO INTEIRA)
        [ 5 ] // (RESTO DA DIVIÃO)
        [ 6 ] SAIR.''')
opção = int(input('SELECIONE UMA DAS OPÇÕES DE ACORDO COM O NÚMERO: '))

if opção == 1:
    print('FUNÇÃO MULTIPLICAÇÃO!')
    num_1 = int(input('DIGITE O PRIMEIRO NÚMERO: '))
    num_2 = int(input('DIGITE O SEGUNDO NÚMERO: '))
    print(f'{num_1} x {num_2} = {num_1 * num_2:.2f}')
elif opção == 2:
    print('FUNÇÃO DIVISÃO!')
    num_1 = int(input('DIGITE O PRIMEIRO NÚMERO: '))
    num_2 = int(input('DIGITE O SEGUNDO NÚMERO: '))
    print(f'{num_1} / {num_2} = {num_1 / num_2:.2f}')
elif opção == 3:
    print('FUNÇÃO POTENCIA!')
    num_1 = int(input('DIGITE O PRIMEIRO NÚMERO: '))
    num_2 = int(input('DIGITE O SEGUNDO NÚMERO: '))
    print(f'{num_1} ** {num_2} = {num_1 ** num_2:.2f}')
elif opção == 4:
    print('FUNÇÃO DIVISÃO INTEIRA!')
    num_1 = int(input('DIGITE O PRIMEIRO VALOR: '))
    num_2 = int(input('DIGITE O SEGUNDO VALOR: '))
    print(f'{num_1} % {num_2} = {num_1 % num_2:.2f}')
elif opção == 5:
    print('FUNÇÃO RESTO DA DIVISÃO')
    num_1 = int(input('DIGITE O PRIMEIRO VALOR: '))
    num_2 = int(input('DIGITE O SEGUNDO VALOR: '))
    print(f'{num_1} // {num_2} = {num_1 // num_2:.2f}')
elif opção == 6:
    print('FINAL!')
else:
    print('OPÇÃO INVALIDA!')
