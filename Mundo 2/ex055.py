pesos = []
q = int(input('Analisar quantas pessoas? '))

for i in range(1, q + 1):
	pesos.append(float(input(f'Peso da {i}ª pessoa: ')))

print(f'\nO maior peso lido foi de {max(pesos)}Kg')
print(f'O menor peso lido foi de {min(pesos)}Kg')
