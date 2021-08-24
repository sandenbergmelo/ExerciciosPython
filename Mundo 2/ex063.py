print('-=' * 11)
print('Sequência de Fibonacci')
print('-=' * 11)

n = int(input('Quantos termos? '))

termo1 = 0
termo2 = 1

print(f'{termo1} → {termo2} ', end='→ ')

i = 3
while i <= n:
	termo_atual = termo1 + termo2
	
	print(f'{termo_atual} ', end='→ ')

	termo1 = termo2
	termo2 = termo_atual
	
	i += 1
else:
	print('FIM')
