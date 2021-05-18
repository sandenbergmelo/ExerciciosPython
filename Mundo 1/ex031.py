dis = float(input('Digite a distância da viagem: '))

if dis > 200:
	valor = dis * 0.45
else:
	valor = dis * 0.5
print(f'A passagem vai custar R${valor:.2f}')
