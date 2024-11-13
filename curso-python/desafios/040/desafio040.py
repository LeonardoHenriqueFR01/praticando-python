# CALCULANDO A MÉDIA desafio 040

print('-=-' * 10)
print('\033[4;33mCALCULANDO MÉDIA\033[m')
print('-=-' * 10)

user = str(input('Qual é o seu nome? '))
nota_1 = float(input(f'{user} qual é a sua primeira nota? '))
nota_2 = float(input(f'{user} qual é a sua segunda nota? '))

media_notas = (nota_1 + nota_2) / 2 

if media_notas >= 5 and media_notas <= 7:
    print(f'Tirando {nota_1} e {nota_2}, a sua média é: {media_notas:.2f}')
    print(f'{user} você está de \033[0;33mRECUPERAÇÃO\033[m!')
elif media_notas >= 7:
    print(f'Tirando {nota_1} e {nota_2}, a sua média é: {media_notas:.2f}')
    print(f'{user} você \033[0;32mPASSOU\033[m!')
elif media_notas < 5:
    print(f'Tirando {nota_1} e {nota_2}, a sua média é: {media_notas:.2f}')
    print(f'{user} você está \033[0;31mREPROVADO\033[m!')
