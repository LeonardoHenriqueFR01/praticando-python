# CRIANDO UM TRIÂNGULO desafio 035

print('-' * 30)
print('\033[4;35;40mCRIANDO UM TRIÂNGULO\033[m')
print('-' * 30)

value_1 = float(input('Qual é o primeiro valor? '))
value_2 = float(input('Qual é o segundo valor? '))
value_3 = float(input('Qual é o terceiro valor? '))

if value_1 + value_2 > value_3 and value_1 + value_3 > value_2 and value_2 + value_3 > value_1:
    print('E possível criar um triângulo!')
else:
    print('Não e possível criar um triângulo!')
