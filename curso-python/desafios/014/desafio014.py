# CONVERSOR DE TEMPERATURA desafio 014


print('-=' * 20)
print(f'{"CONVERSOR DE TEMPERATURA":-^40}')
print('-=' * 20)

graus_c = float(input('DIGITE A TEMPERATURA EM °C: '))
kelvin = graus_c + 273.15
fahrenheit = (graus_c * 9 / 5) + 32

print(f'{graus_c}°C CONVERTIDOS PARA KELVIN SÃO: {kelvin:.2f}K')
print(f'{graus_c}°C CONVERTIDOS PARA FAHRENHEIT SÃO: {fahrenheit:.2f}°F')
