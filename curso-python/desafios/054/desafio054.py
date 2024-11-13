# GRUPO DE MAIORIDADE desafio 054

from datetime import date

print('-' * 40)
print('GRUPO DE MAIORIDADE')
print('-' * 40)

atual = date.today().year
totalmaior = 0
totalmenor = 0
for i in range(1, 8):
    ano = int(input(f'Em que ano a {i} pessoa nasceu? '))
    idade = atual - ano
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'Ao todo tivemos {totalmaior} pessoas maiores de idade!')
print(f'Ao todo tivemos {totalmenor} pessoas menores de idade!')
