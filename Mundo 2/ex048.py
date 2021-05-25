s = 0
v = 0
for i in range(1, 501, 2):
	if (i % 3 == 0):
		s += i
		v += 1

print(f'A soma de todos {v} valores é igual a {s}')
