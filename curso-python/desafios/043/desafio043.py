# CALCULANDO SEU IMC desafio 043

print('-=-' * 10)
print('CALCULANDO SEU IMC')
print('-=-' * 10)

peso = float(input('Qual é o seu peso? (Kg) ' ))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de: {imc:.1f}!')

if imc < 18.5:
    print('Você está ABAIXO do peso normal!')
elif 18.5 <= imc < 25:
    print('PARABÊNS, você está na faixa de peso NORMAL!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBSIDADE!')
elif imc >= 40:
    print('Você está em OBSIDADE MÓRBIDA, cuidado!')
