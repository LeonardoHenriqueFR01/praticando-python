# FAZENDO UM PEDIDO EM UM RESTAURANTE

from time import sleep

print('\033[33m-=\033[m' * 20)
print(f'\033[4;35m{"RESTAURANTE":-^40}\033[m')
print('\033[33m-=\033[m' * 20)

user = str(input('Qual é o seu nome? '))
print(f'Olá {user}! Seja Bem-Vindo.')
print('\033[33m-\033[m' * 40)

print('Irei te mostrar o cardapio!')
print('Espere um pouco...')
sleep(3)
print('\033[33m-\033[m' * 40)

print(f'\033[4;32m{"ENTRADAS":^40}\033[m')
print('\033[33m-\033[m' * 40)
print('''AQUI ESTÃO AS OPÇÕES:
\033[34m[ 1 ] Bruschettas de tomate e manjericão.\033[m
      
\033[34m[ 2 ] Bolinhos de bacalhau ou de queijo.\033[m
      
\033[34m[ 3 ] Dadinhos de tapioca com molho de \nmelado e pimenta.\033[m''')

list_entradas = {1:'Bruschettas de tomate e manjericão', 2:'Bruschettas de tomate e manjericão', 3:'Dadinhos de tapioca com molho de melado e pimenta'}

print('\033[33m-\033[m' * 40)
entrada = int(input(f'Qual vai ser a entrada Sr {user}? '))
print('Ok Bela escolha!')
print('Vamos para o prato principal...')
sleep(3)

print('\033[33m-\033[m' * 40)
print(f'\033[4;32m{"PRINCIPAL":^40}\033[m')
print('\033[33m-\033[m' * 40)
print('''AQUI ESTÃO AS OPÇÕES:
\033[34m[ 1 ] Risoto de cogumelos com parmesão.\033[m
      
\033[34m[ 2 ] Bife à parmegiana com arroz e batatas.\033[m
      
\033[34m[ 3 ] Filé de frango grelhado com legumes \nao vapor.\033[m''')

list_principal = {1:'Risoto de cogumelos com parmesão', 2:'Bife à parmegiana com arroz e batatas', 3:'Filé de frango grelhado com legumes ao vapor'}

print('\033[33m-\033[m' * 40)
principal = int(input(f'Qual vai ser o prato principal Sr {user}? '))
print('Ok bela escolha!')
print('Vamos para a Sobremesa...')
sleep(3)

print('\033[33m-\033[m' * 40)
print(f'\033[4;32m{"SOBREMESA":^40}\033[m')
print('\033[33m-\033[m' * 40)
print('''AQUI ESTÃO AS OPÇÕES:
\033[34m[ 1 ] Petit gâteau com sorvete de baunilha.\033[m
      
\033[34m[ 2 ] Pudim de leite condensado.\033[m
      
\033[34m[ 3 ] Mousse de maracujá.\033[m''')

list_sobremesa = {1:'Petit gâteau com sorvete de baunilha', 2:'Pudim de leite condensado', 3:'Mousse de maracujá'}

print('\033[33m-\033[m' * 40)
sobremesa = int(input(f'Qual vai ser a Sobremesa Sr {user}? '))
print('Ok bela escolha!')
print('Vamos para as bebidas...')
sleep(3)

print('\033[33m-\033[m' * 40)
print(f'\033[4;32m{"BEBIDAS":^40}\033[m')
print('\033[33m-\033[m' * 40)
print('''AQUI ESTÃO AS OPÇÕES:
\033[34m[ 1 ] Sucos naturais (laranja, abacaxi com hortelã, melancia).\033[m
      
\033[34m[ 2 ] Smoothie de frutas vermelhas.\033[m
      
\033[34m[ 3 ] Chá gelado de hibisco com limão.\033[m''')

list_bebidas = {1:'Sucos naturais', 2:'Smoothie de frutas vermelhas', 3:'Chá gelado de hibisco com limão'}

print('\033[33m-\033[m' * 40)
bebidas = int(input(f'Qual vai ser a bibida Sr {user}? '))
print('Ok bela escolha!')
