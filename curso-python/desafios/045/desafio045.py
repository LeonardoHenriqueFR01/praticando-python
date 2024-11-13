from time import sleep
from random import randint

print('-=-' * 8)
print('------JOKENPO------')
print('-=-' * 8)

user = str(input('Qual é o seu nome? '))
print('''
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogada = int(input(f'{user}, QUAL É A SUA JOGADA: '))
comput = randint(1, 3)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=-' * 8)

# Mapear jogadas para exibir corretamente o que cada um jogou
opcoes = {1: 'PEDRA', 2: 'PAPEL', 3: 'TESOURA'}
print(f'COMPUTADOR JOGOU {opcoes[comput]}')
print(f'{user} JOGOU {opcoes[jogada]}')

# Regras do jogo
if jogada == comput:
    print('EMPATE WOW')
elif (jogada == 1 and comput == 3) or (jogada == 2 and comput == 1) or (jogada == 3 and comput == 2):
    print(f'{user} VENCEU!')
else:
    print('COMPUTADOR VENCEU!')
print('-=-' * 8)
