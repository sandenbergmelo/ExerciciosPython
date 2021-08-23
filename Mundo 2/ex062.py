print('Gerador de PA')
print('-=' * 10)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

total = 0
mais = 10

i = 1
while mais != 0:
	total += mais
	while i <= total:
		print(f'{a1} → ', end='')
		a1 += r
		i += 1
	else:
		print('PAUSA')
	mais = int(input('Mais quantos termos? '))
else:
	print(f'Progressão finalizada com {total} termos')
