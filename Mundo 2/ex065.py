soma = n = quantidade_de_numeros = 0
numeros = []
continuar = 'S'

while continuar == 'S':
	n = int(input('Digite um número: '))
	continuar = str(input('Quer continuar? [S/N]: ')).upper()
	numeros.append(n)
	quantidade_de_numeros += 1
	soma += n
else:
	m = soma / quantidade_de_numeros
	print(f'\nA média entre os {quantidade_de_numeros} números digitados é: {m}')
	print(f'O menor número é {min(numeros)} e o maior é {max(numeros)}')
