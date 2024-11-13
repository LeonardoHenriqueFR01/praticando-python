# SISTEMA DE RADAR desafio 029


print('-=' * 20)
print(f'{"SISTEMA DE RADAR":-^40}')
print('-=' * 20)

km = float(input('QUANTOS (KM) VOCÊ ULTRAPASSOU NO RADAR? '))
multa = (km - 80) * 7

if km >= 81:
    print('VOCÊ UTRAPASSOU O LIMITE DE VELOCIDADE')
    print(f'VOCÊ DEVERA PAGAR UMA MULTA NO VALOR DE: R${multa:.2f}')
else:
    print('VOCÊ PASSOU ABAIXO DO LIMITE DE VELOCIDADE')
