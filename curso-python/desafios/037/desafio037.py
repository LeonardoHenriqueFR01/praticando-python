# CONVERTENDO NÚMEROS PARA BINÁRIO OCTAL HEXADECIMAL desafio 037

print('-=-' * 10)
print('\033[0;35mOCTAL HEXACIMAL É BINÁRIO\033[m')
print('-=-' * 10)

user_num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de converção: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] comverter para HEXADECIMAL''')
user_opção = int(input('Sua opção: '))

if user_opção == 1:
    print(f'{user_num} convertido para BINÁRIO é igual a: {bin(user_num)[2:]}!')
elif user_opção == 2:
    print(f'{user_num} convertidos para OCTAL é igual a: {oct(user_num)[2:]}!')
elif user_opção == 3:
    print(f'{user_num} convertidos para HEXADECIMAL é igual a: {hex(user_num)[2:]}!')
else:
    print('Opção invalida . Tente novamente.')
