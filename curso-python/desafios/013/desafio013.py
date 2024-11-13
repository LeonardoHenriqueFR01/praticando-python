# AUMENTO DE 15% NO SALÁRIO desafio 013


print('-=' * 20)
print(f'{"AUMENTO DE 15% NO SALÁRIO":-^40}')
print('-=' * 20)

salario = float(input('QUAL É O SEU SALÃRIO ATUAL: R$'))
aumento_15 = 15 * salario / 100
salario_atal = salario + aumento_15

print(f'O SEU SALÁRIO ERA DE: R${salario:.2f}')
print(f'COM UM AUMENTO DE 15%')
print(f'AGORA VOCE VAI RECEBER R${salario_atal:.2f}')
