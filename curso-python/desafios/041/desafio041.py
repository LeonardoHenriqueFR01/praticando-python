# CLASSIFICANDO ATLETAS desafio 041

from datetime import datetime

print('-=-' * 7)
print('\033[4;33mANALISANDO ATLETAS\033[m!')
print('-=-' * 7)

user = str(input('Qual é o nome do atleta? '))
year = int(input('Qual é o seu ano de nascimento? '))
print('-' * 74)

year_atual = datetime.now().year
idade_user = year_atual - year

if idade_user <= 9:
    print(f'O atleta de nome {user} e tem {idade_user} anos de idade considerado como: MIRIM!') # para quem nasceu de 2015 até o ano atual
elif idade_user > 9 and idade_user < 15:
    print(f'O atleta de nome {user} e tem {idade_user} anos de idade considerado como: INFANTIL!') # para quem nasceu de 2010 até o ano atual
elif idade_user > 14 and idade_user < 20:
    print(f'O atleta de nome {user} e tem {idade_user} anos de idade considerado como: JUNIOR!') # para quem nasceu de 2005 até o ano atual
elif idade_user > 19 and idade_user < 26:
    print(f'O atleta de nome {user} e tem {idade_user} anos de idade considerado como: SÊNIOR!') # para quem nasceu de 1999 até o ano atual
else:
    print(f'O atleta de nome {user} e tem {idade_user} anos de idade considerado como: MASTER!') # para quem nasceu de 1998 para baixo
 