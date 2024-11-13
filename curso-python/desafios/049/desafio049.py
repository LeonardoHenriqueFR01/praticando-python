# TABUADA V2 desafio 049

print('-=' * 10)
print('TABUADA V2')
print('-=' * 10)

num_tab = int(input('Digite o número da TABUADA: '))

for c in range(1, 11):
    print(f'{num_tab} x {c} = {num_tab * c}')
