n = int(input('Calcular fatorial de: '))

c = n
f = 1
print(f'{n}! = ', end='')
while c >= 1:
	print(f'{c}', end='')
	print(' x ' if c > 1 else ' = ', end='')
	f *= c
	c -= 1
print(f)
