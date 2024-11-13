# ACERTANDO UM NÚMERO DE 0 A 5 desafio 028

from random import randint
from time import sleep

print('ACERTE O NÚMERO DE 0 A 5')

num = int(input('DIGITE O SEU NÚMERO: '))
num_sort = randint(1, 5)

print('GERANDO NÚMERO...')
sleep(2)
print(f'O NÚMERO SORTEADO FOI: {num_sort}')

if num == num_sort:
    print('ACERTOU')
else:
    print('ERROU')
