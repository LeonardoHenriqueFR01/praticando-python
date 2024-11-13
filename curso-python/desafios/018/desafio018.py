# SENO COSSENO E TANGENTE desafio 018

from math import sin, cos, tan, radians

angulo = float(input('DIGITE UM ÂNGULO QUAL QUER: '))

angulo_ran = radians(angulo)

print(f'PARA O ÂNGULO DE: {angulo}°')
print(f'O SEU SENO SERIA DE: {sin(angulo_ran):.2f}')
print(f'O SEU COSSENO DERIA DE: {cos(angulo_ran):.2f}')
print(f'E O SEU TANGENTE SERIA DE: {tan(angulo_ran):.2f}')
