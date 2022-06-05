velocidade = float(input('Velocidade do veículo em km/h: '))

if velocidade > 80:
	multa = (velocidade - 80) * 7
	print('Você ultrapassou o limite de 80km/h')
	print(f'Pagará uma multa de R${multa:.2f}')
else:
	print(f'Velocidade de {velocidade}km/h')
	print('Sem multa')
