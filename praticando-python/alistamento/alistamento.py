# SISTEMA DE ALISTAMENTO CRIADO POR Leonardo Henrique

from datetime import datetime
from time import sleep

print('\033[0;36m-=-\033[m' * 8)
print('\033[4;35mSISTEMA DE ALISTAMENTO\033[m')
print('\033[0;36m-=-\033[m' * 8)

print('''PRIMEIRO SELECIONE SEU SEXO:
\033[0;33m[ 1 ] MASCULINO\033[m
\033[0;34m[ 2 ] FEMININO\033[m''')
print('\033[0;35m=\033[m' * 30)
sexo = int(input('Selecione aqui seu sexo: '))
user = str(input('Qual é o seu nome? '))
ano_nasci = int(input(f'{user} qual é o seu ano de nascimento? '))
ano_atual = datetime.now().year
user_idade = ano_atual - ano_nasci

print('\033[0;33mANALISANDO DADOS...\033[m')
sleep(3)
print('\033[0;35m=\033[m' * 60)

if sexo == 1 and user_idade < 18:
    ano_alista = ano_nasci + 18
    print(f'{user} você não pode se \033[0;33mALISTAR ainda\033[m!')
    print(f'Você deve se \033[0;33malistar\033[m no ano de {ano_alista}!')
elif sexo == 1 and user_idade == 18:
    print(f'{user} você deve se alistar \033[0;31mIMEDIATAMENTE\033[m!')
    print(f'Pois você já está com {user_idade} anos de idade, neste caso você ja pode se \033[0;31mALISTAR\033[m!')
elif sexo == 1 and user_idade > 18:
    ano_alista = ano_nasci + 18
    print(f'{user} já passou da hora de você fazer o \033[0;31mALISTAMENTO\033[m caso não tenha se \033[0;31mALISTADO\033[m!')
    print(f'Caso você já tenha se \033[0;32mALISTADO\033[m espero que tenha sido no ano de {ano_alista}!')
else:
    print('SEXO \033[0;31mINVALIDO\033[m')

if sexo == 2:
    print('\033[4;33mMULHERES NÃO PRECISAM SE ALISTAR NO BRASIL!\033[m')

print('\033[0;35m=\033[m' * 60)

print('\033[0;36m-=-\033[m' * 13)
print('\033[4;35mAPERTE F5 PARA SE CANDIDATAR NOVAMENTE!\033[m')
print('\033[0;36m-=-\033[m' * 13)
