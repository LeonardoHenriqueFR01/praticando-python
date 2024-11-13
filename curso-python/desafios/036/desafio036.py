# APROVANDO UM EMPRESTIMO PARA A COMPRA DE UMA CASA desafio 036

print('-=-' * 10)
print('\033[0;35mAPROVANDO UM EMPRESTIMO\033[m')
print('-=-' * 10)

user = str(input('Qual é o seu nome? '))
value_house = float(input(f'{user} qual é o valor da casa? Que você deseja comprar: R$'))
salario = float(input('Qual é o seu salário? R$'))
tempo = int(input(f'{user} em quanto anos você pretende pagar a casa? '))
print('-' * 30)

meses_parcelas = 12 * tempo
value_parcelas = value_house / meses_parcelas
porcento_30 = (30 / 100 * salario)

print(f'Meses pagando a casa: {meses_parcelas}')
print(f'Valor das parcelas será: R${value_parcelas:.2f}')

if value_parcelas <= porcento_30:
    print(f'{user} o valor das parcelas não passaram de 30% do seu salário seu emprestimo podera ser concluido!')
else:
    print(f'{user} o valor das parcelas passaram de mais de 30% do seu salário infelizmente não podera fazer o emprestimo!')

print('-' * 30)
print('APERTE F5 PARA TENTAR NOVAMENTE!')
print('-' * 30)
