n = int(input('Digite um número: '))
d = 0

for i in range(1, n + 1):
	if n % i == 0:
		print('\033[32m', end='')
		d += 1
	else:
		print('\033[31m', end='')
	print(i, end=' ')

print(f'\n\033[mO número {n} foi divisível {d} vezes')
if d == 2:
	print(f'É primo')
else:
	print(f'Não é primo')
