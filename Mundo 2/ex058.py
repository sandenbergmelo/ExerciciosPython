from random import randint

n = randint(0, 10)

print('Pensei em um número entre 0 e 10')
palpite = int(input('Adivinhe qual é: '))

tentativas = 1
while n != palpite:
	tentativas += 1
	if n > palpite:
		palpite = int(input('Maior: '))
	else:
		palpite = int(input('Menor: '))
else:
	print(f'Você acertou em {tentativas} tentativas!')
	print(f'Eu pensei no número {n}')
