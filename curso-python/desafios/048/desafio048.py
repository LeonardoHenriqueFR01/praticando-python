# NÚMEROS IMPARES MULTPLIPOS DE 3 DE 3 ATÉ 500 desafio 048

from time import sleep

print('-=' * 15)
print('NÚMEROS IMPARES MULTIPLOS DE 3')
print('DE 3 ATÉ 500')
print('-=' * 15)

soma = 0
cont = 1

for c in range(3, 501, 6):
    print(f'{c}', end = ' ')
    sleep(0)
    cont = cont + 1
    soma = soma + c

print(' ' * 40)
print(f'\nA soma de todos os {cont} valores solicitados é {soma}!')
