n = soma = quantidade_de_numeros = 0
while n != 999:
	n = int(input('Digite um número [999 para parar]: '))
	if n != 999:
		quantidade_de_numeros += 1
		soma += n
else:
	print(f'{quantidade_de_numeros} números digitados')
	print(f'A soma entre eles é igual a {soma}')
