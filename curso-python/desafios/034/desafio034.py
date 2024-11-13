# CALCULANDO UM AUMENTO DE SALÁRIO desafio 034

print('-' * 40)
print('\033[0;33mCALCULANDO UM AUMENTO DE SALÁRIO\033[m')
print('-' * 40)

user = str(input('Qual é o seu nome? '))
salario = float(input(f'{user} qual é o seu salário? '))

if salario >= 1250:
    aumento_10 = salario * (10 / 100) + salario
    print(f'{user} o seu antigo salário era de R${salario:.2f} e agora é de R${aumento_10:.2f}!')
else:
    aumento_15 = salario * (15 / 100) + salario
    print(f'{user} o seu antigo salário era de R${salario:.2f} e agora é de R${aumento_15:.2f}!')
