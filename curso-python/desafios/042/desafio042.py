# ANALISANDO TRIÂNGULOS desafio 042

print('-=-' * 10)
print('ANALISANDO UM TRIÂNGULO')
print('-=-' * 10)

value_1 = float(input('Qual é o primeiro valor? '))
value_2 = float(input('Qual é o segundo valor? '))
value_3 = float(input('Qual é o terceiro valor? '))

if value_1 + value_2 > value_3 and value_1 + value_3 > value_2 and value_2 + value_3 > value_1:
    print('E possível criar um triângulo!', end=' ')
    if value_1 == value_2 == value_3:
        print('EQUILÁTERO!')
    elif value_1 != value_2 != value_3 != value_1:
        print('ESCALENO')
    else:
        print('ISÓCELES!')
else:
    print('Não e possível criar um triângulo!')
