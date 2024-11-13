# CALCULANDO UM ANO BISSEXTO desafio 032

from datetime import date

print('-' * 30)
print('CALCULANDO SE O ANO E BISSEXTO')
print('-' * 30)

ano = int(input('Qual é o ano que você deseja analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é (BISSEXTO)!')
else:
    print(f'O ano {ano} não é (BISSEXTO)!')
