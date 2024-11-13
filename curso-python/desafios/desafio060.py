# CALCULANDO O FATORIAL DE UM NÚMERO desafio 060

num = int(input('Digite um número: '))
fatorial = 1

for i in range(1, num + 1):
    fatorial *= i
print(f'O fatorial de {num} é {fatorial}!')
