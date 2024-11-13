#CALCULANDO VALOR DA VIAGEM desafio 031

print('-' * 30)
print('CALCULANDO VALOR DA VIAGEM!')
print('-' * 30)

distancia = float(input('Qual é a distancia da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia}km !')

if distancia <= 200:
    presço = distancia * 0.50
else:
    preço = distancia * 0.45

print(f'O preço da sua passagem será R${preço:.2f}!')
