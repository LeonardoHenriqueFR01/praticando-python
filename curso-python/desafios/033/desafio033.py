# QUAL É O VALOR MAIOR E MENOR desafio 033

print('-' * 30)
print('QUAL É O VALOR MAIOR E O MENOR')
print('-' * 30)

value_1 = int(input('Digite o primeiro valor: '))
value_2 = int(input('Digite o segundo valor: '))
value_3 = int(input('Digite o terceiro valor: '))

menor = value_1
if value_2 < value_1 and value_2 < value_3:
    menor = value_2
if value_3 < value_1 and value_3 < value_2:
    menor = value_3

maior = value_1
if value_2 > value_1 and value_2 > value_3:
    maior = value_2
if value_3 > value_1 and value_3 > value_2:
    maior = value_3

print(f'O maior valor digitado foi: {maior}')    
print(f'O menor valor digitado foi: {menor}')
