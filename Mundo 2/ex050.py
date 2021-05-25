s = 0
v = 0

for i in range(1, 7):
	n = int(input(f'Digite o {i}º número: '))
	if n % 2 == 0:
		s += n
		v += 1

print(f'A somas dos {v} números PARES digitados é igual a {s}')
