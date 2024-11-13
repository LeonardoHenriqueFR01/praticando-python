# VALOR A SER PAGO PELO PRODUTO

print('\033[0;35m-=-\033[m' * 10)
print('\033[4;33m-------SUPERMECADOS BH-------\033[m')
print('\033[0;35m-=-\033[m' * 10)

user = str(input('Qual é o seu nome? '))
print(f'Prazer {user}!')
print('-' * 50)

valor_compra = float(input('QUAL FOI O VALOR TOTAL DA SUA COMPRA? R$'))
print('-' * 50)

print('''AQUI ESTÃO AS FORMAS DE PAGAMENTO
\033[0;34m[ 1 ] Á VISTA DINHEIRO / PIX\033[m
\033[0;32m[ 2 ] Á VISTA NO CARTÃO\033[m
\033[0;33m[ 3 ] 2X NO CARTÃO\033[m
\033[0;31m[ 4 ] 3X OU MAIS NO CARTÃO\033[m''')
print('-' * 45)

opção = int(input(f'{user} SELECIONE A FORMA DE PAGAMENTO: '))
print('-' * 45)

if opção == 1:
    desconto_10 = (10 / 100 * valor_compra)
    preço = valor_compra - desconto_10 
    print(f'\033[0;34m{user} SUA COMPRA FOI DE R${valor_compra:.2f}, VOCÊ PAGARA O VALOR DE R${preço:.2f}!\033[m')
elif opção == 2:
    desconto_5 = (5 / 100 * valor_compra)
    preço = valor_compra - desconto_5
    print(f'\033[0;32m{user} SUA COMPRA FOI DE R${valor_compra:.2f}, VOCÊ PAGARA O VALOR DE R${preço:.2f}!\033[m')
elif opção == 3:
    print(f'\033[0;33m{user} SUA COMPRA FOI DE R${valor_compra:.2f}, VOCÊ PAGARA O VALOR DE R${valor_compra:.2f}!\033[m')
elif opção == 4:
    juros_20 = (20 / 100 * valor_compra)
    preço = valor_compra + juros_20
    print(f'\033[0;31m{user} SUA COMPRA FOI DE R${valor_compra:.2f}, VOCÊ PAGARA O VALOR DE R${preço:.2f}!\033[m')
