# DIGITE UM NÚMERO E VEJA A RAIZ QUADRADA DELE

from math import sqrt

print('-' * 30)
print('DIGITE UM NÚMERO E VEJA A RAIZ QUADRADA DELE')
print('-' * 30)

num = int(input('Digite o número que você deseja saber a raiz quadrada: '))
raiz = sqrt(num)

print(f'O número que você digitou foi {num} a raiz-quadrada dele é: {raiz:.2f}')
