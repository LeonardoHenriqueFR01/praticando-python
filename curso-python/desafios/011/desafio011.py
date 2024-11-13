# CALCULANDO UMA PAREDE desafio 011


largura = float(input('QUAL É A LARGURA DA PAREDE EM (m): '))
altura = float(input('QUAL É A ALTURA DA PAREDE EM (m): '))

metros_2 = largura * altura / 2

print(f'UMA PAREDE COM {largura:.2f} METROS DE LARGURA')
print(f'É COM UMA ALTURA DE {altura} METROS')
print(f'SABENDO QUE A CADA 2m QUADRADOS VOCÊ GASTA 1 LITRO DE TINTA')
print(f'ENTÃO VOCE VAI PRECISAR DE {metros_2:.2f} LITROS DE TINTA PARA PINTAR ESSA PAREDE!')
