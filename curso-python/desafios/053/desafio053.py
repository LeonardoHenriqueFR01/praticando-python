# DETECTOR DE PALINDROMO desafio 053


print('-' * 40)
print('DETECTOR DE PALÍNDROMO!')
print('-' * 40)

frase = str(input('DIGITE UMA FRASE: '))
palavras = frase.split()
junto = ''.join(palavras)
inverso = '' # inverso = junto[::-1] pode ser assim também

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}!')
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')
