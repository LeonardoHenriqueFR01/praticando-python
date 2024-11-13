#DIGITE UM NÚMERO E VEJA A TABUADA DELE

from time import sleep

print('-' * 40)
print('TABUADA DE MULTIPLICAÇÃO')
print('-' * 40)

value_tab = int(input('Digite o número que você deseja ver a tabuada: '))
print(f'OK VAMOS GERAR A TABUADA DO: {value_tab}!')
print('-' * 40)

print('GERANDO TABUADA...')
sleep(4)
print('-' * 40)

x1 = value_tab * 1
x2 = value_tab * 2
x3 = value_tab * 3
x4 = value_tab * 4
x5 = value_tab * 5
x6 = value_tab * 6
x7 = value_tab * 7
x8 = value_tab * 8
x9 = value_tab * 9
x10 = value_tab * 10

print(f'AQUI ESTÁ A TABUDA DO {value_tab}')
print('=' * 40)
print(f'{value_tab} x 1 = {x1}')
print(f'{value_tab} x 2 = {x2}')
print(f'{value_tab} x 3 = {x3}')
print(f'{value_tab} x 4 = {x4}')
print(f'{value_tab} x 5 = {x5}')
print(f'{value_tab} x 6 = {x6}')
print(f'{value_tab} x 7 = {x7}')
print(f'{value_tab} x 8 = {x8}')
print(f'{value_tab} x 9 = {x9}')
print(f'{value_tab} x 10 = {x10}')
print('=' * 40)
