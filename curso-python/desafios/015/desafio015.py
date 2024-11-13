# ALUGUEL DE CARROS desafio 014


print('-=' * 20)
print(f'{"ALUGUEL DE CARROS":-^40}')
print('-=' * 20)


dias = int(input('POR QUANTOS DIAS O CARRO FOI ALUGADO: '))
km = float(input('QUANTOS (KMs) FORAM PERCORRIDOS: '))

valor_pagar = (dias * 60) + (km * 0.15)

print(f'O VALOR A SER PAGO PELO ALUGUEL DO CARRO É DE: R${valor_pagar:.2f}')
