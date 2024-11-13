# MAIOR E MENOR DA SEQUÊNCIA desafio 055

print('-=' * 20)
print(f'{"MAIOR E MENOR DA SEQUÊNCIA":^40}')
print('-=' * 20)

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'PESO DA {p}° PESSOA: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O MAIOR PESO LIDO FOI DE {maior}Kg')
print(f'O MENOR PESO LIDO FOI DE {menor}Kg')
