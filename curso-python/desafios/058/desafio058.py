# ACERTE O NÚMEROS SORTEADO desafio 058

from random import randint

num_sort = randint(1, 10)
print('PENSEI EM UM NÚMERO ENTRE 1 E 10 TENTE ADVINHAR.')
print('SERÁ QUE VOCÊ CONSEGUE ADIVINHAR QUAL FOI?')
print('-' * 40)
acertou = False
tentativas = 0 

while not acertou:
    num_user = int(input('QUAL É O SEU PALPITE: '))
    tentativas += 1
    if num_sort == num_user:
        acertou = True
    else:
        if num_user < num_sort:
            print('MAIS... TENTE NOVAMENTE!')
        elif num_user > num_sort:
            print('MENOS... TENTE NOVAMENTE')

print(f'ACERTOU COM {tentativas} TENTATIVAS. PARABÊNS!')
print(f'O NÚMERO SORTEADO FOI: {num_sort}')
