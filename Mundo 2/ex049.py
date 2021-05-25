n = int(input('Digite um número para ver sua tabuada: '))

print('-=' * 6)
for i in range(1, 11):
	print(f'{n} x {i:2} = {n * i:2}')
print('-=' * 6)
