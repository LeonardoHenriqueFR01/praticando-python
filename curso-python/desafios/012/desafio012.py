# CALCULANDO 5% DE DESCONTO desafio 012

print('-=' * 20)
print(f'{"CALCULANDO 5% DE DESCONTO":-^40}')
print('-=' * 20)

produto = float(input('QUAL É O PREÇO DO PRODUTO: R$'))
desconto_5 = 5 * produto / 100
preço = produto - desconto_5

print(f'O PREÇO DO PRODUTO CUSTA: R${produto:.2f}')
print(f'COM 5% DE DESCONTO AGORA ELE VAI CUSTAR: R${preço:.2f}')
