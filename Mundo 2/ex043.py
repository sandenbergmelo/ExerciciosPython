peso = float(input('Digite o peso em Kg: '))
altura = float(input('Digite a altura em m: '))
imc = peso / altura ** 2

print(f'IMC de {imc:.1f}')
if imc < 18.5:
	print('Abaixo do peso!')
elif imc < 25:
	print('Peso ideal.')
elif imc < 30:
	print('Sobrepeso!')
elif imc < 40:
	print('Obesidade!')
else:
	print('Obesidade mórbida! CUIDADO!')
