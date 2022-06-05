frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
inverso = frase[::-1]

print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
	print('A frase é um palíndromo')
else:
	print('A frase não é um palíndromo')
