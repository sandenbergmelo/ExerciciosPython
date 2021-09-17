soma = cont = 0
while True:
	n = int(input('Digite um número [999 para finalizar]: '))
	if n == 999:
		break
	cont += 1
	soma += n
print(f'\nA soma entre os {cont} valores é igual a {soma}.')
