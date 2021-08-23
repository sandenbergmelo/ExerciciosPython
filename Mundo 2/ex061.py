print('Gerador de PA')
print('-=' * 10)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

i = 1
while i <= 10:
	print(f'{a1} → ', end='')
	a1 += r
	i += 1
else:
	print('Fim')
