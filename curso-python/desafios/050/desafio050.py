# SOMANDO NÚMEROS PARES desafio 050


soma = 0
cont = 0

for c in range(1, 7):
    num = int(input('DIGITE UM NÚMERO: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você digitou {cont} números e a soma deles foi: {soma}!')
