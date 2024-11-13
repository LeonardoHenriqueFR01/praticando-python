#CALCULANDO O VALOR DA HIPOTENUSA

from math import hypot
from time import sleep

print('-' * 20)
print('ACHANDO O VALOR DA HIPOTENUSA')
print('-' * 20)

value_ca_oposto = float(input('Digite o valor do cateto oposto: '))
value_ca_adjacente = float(input('Digite o valor do cateto adjacente: '))
print('-' * 20)

valor_hipotenusa = hypot(value_ca_oposto, value_ca_adjacente)

print('GERANDO O VALOR DA HIPOTENUSA...')
sleep(5)

print(f'O valor do cateto oposto é: {value_ca_oposto}')
print(f'O valor do cateto adjacente é: {value_ca_adjacente}')
print(f'O VALOR DA HIPOTENUSA É: {valor_hipotenusa:.2f}')
