# LENDO O SEXO DE UMA PESSOA desafio 057

sexo = str(input('INFORME O SEU SEXO [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('INFORME O SEU SEXO [M/F]: ')).strip().upper()[0]

print(f'SEXO {sexo} REGISTRADO COM SUCESSO!')
