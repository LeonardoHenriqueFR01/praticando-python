# ALISTAMENTO desafio 039

from datetime import datetime

print('-=-' * 10)
print('\033[0;35mVERIFICANDO ALISTAMENTO\033[m')
print('-=-' * 10)
 
user = str(input('Qual é o seu nome? '))
user_year = int(input('Qual é o seu ano de nascimento? '))

ano_atual = datetime.now().year
user_idade = ano_atual - user_year
ano_18 = user_year + 18

print(f'Certo você está com {user_idade} anos de idade!')

if user_idade < 18:
    print(f'{user} ainda faltam {user_idade - 18} anos para o seu alistamento!')
    print(f'Seu alistamento será em {ano_18}!')
elif user_idade == 18:
    print(f'{user} Está no momento certo de você se alistar!')
else:
    print(f'{user} já passou da hora de você se alistar!')
