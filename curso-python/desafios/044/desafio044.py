# CALCULANDO VALOR A SER PAGO PELO PRODUTO desafio 044

print('-=-' * 15)
print('VALOR A SER PAGO PELO PRODUTO')
print('-=-' * 15)

produto = str(input('Qual é o produto que você deseja comprar? '))
valor_prod = float(input('Qual é o valor deste produto? R$'))
print('-' * 90)

desconto_10 = (10 / 100 * valor_prod)
desconto_5 = (5 / 100 * valor_prod)
juros_20 = (20 / 100 * valor_prod)

print('''OPÇÕES DE PAGAMENTO
[ 1 ] Á VISTA DINHEIRO/PIX
[ 2 ] A VISTA NO CARTÃO
[ 3 ] 2x NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
opção = int(input('SELECIONE A OPÇÃO: '))
print('-' * 90)

if opção == 1:
    preço = valor_prod - desconto_10
    print(f'Você ganhou 10% de desconto no produto e pagara R${preço:.2f} no produto!')
elif opção == 2:
    preço = valor_prod - desconto_5
    print(f'Você ganhou 5% de desconto no produto e pagara R${preço:.2f} no produto!')
elif opção == 3:
    print(f'Você pagara R${valor_prod:.2f} no produto não conseguimos desconto nesta opção!')
elif opção == 4:
    preço = valor_prod + juros_20
    print(f'Você pagara R${preço:.2f} no produto não conseguimos desconto nesta opção!')
