# CATETO DE UM TRIANGULO desafio 017

from math import hypot

cateto_o = float(input('DIGITE O VALOR DO CATETO OPOSTO: '))
cateto_a = float(input('DIGITE O VALOR DO CATETO ADJACENTE: '))

hipotesuna = hypot(cateto_o, cateto_a)

print(f'O VALOR DO CATETO OPOSTO FOI: {cateto_o}')
print(f'O VALOR DO CATETO ADJACENTE FOI: {cateto_a}')
print(f'SENDO ASSIM O VALOR DA HIPOTENUSA VAI SER DE: {hipotesuna:.2f}')
