# ANALISADOR DE PESO desafio 056

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
totmulher20 = 0

for a in range(1, 5):
    print(f'{f"{a}° PESSOA":-^20}')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    soma_idade += idade

    if a == 1 and sexo in 'Mn':
        maior_idade_homem = idade
        nome_velho = nome
    
    if sexo in 'Mn' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome

    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

media_idade = soma_idade / 4

print(f'A MÉDIA DE IDADE DO GRUPO É DE {media_idade} anos')
print(f'O HOMEM MAIS VELHO TEM {maior_idade_homem} E SE CHAMA {nome_velho}')
print(f'AO TODO SÃO {totmulher20} MULHERES COM MENOS DE 20 ANOS')
