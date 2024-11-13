# CONTAGEM REGRESSIVA DE FOGOS DE ARTIFICIO desafio 046

from time import sleep

print('-=' * 20)
print('\033[0;31mCONTAGEM REGRESSIVA FOGOS DE ARTIFICIO\033[m')
print('-=' * 20)

print('CONTAGEM REGRESSIVA...')
sleep(2)

for c in range(10, 0, -1):
    print(c)
    sleep(1)

print('\033[4;33mBOOM FOGOS EXPLODINDO\033[m')
