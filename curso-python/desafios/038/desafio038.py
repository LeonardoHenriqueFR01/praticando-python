# MAIOR MENOR OU IGUAL desafio 038

print('-=-' * 10)
print('\033[0;35mMAIOR, MENOR OU IGUAL\033[m')
print('-=-' * 10)

user_num_1 = int(input('Digite o primeiro número: '))
user_num_2 = int(input('Digite o segundo número: '))

if user_num_1 > user_num_2:
    print(f'O primeiro valor que foi: {user_num_1} é MAIOR que o segundo que foi: {user_num_2}!')
elif user_num_2 > user_num_1:
    print(f'O segundo valor que foi: {user_num_2} e MAIOR que o primeiro que foi: {user_num_1}!')
elif user_num_1 == user_num_2:
    print(f'O primeiro valor que foi: {user_num_1} e o segundo que foi: {user_num_2} são IGUAIS!')

