sal = float(input('Digite o valor do salário R$'))

if sal > 1250:
	novoSal = sal * 1.1
else:
	novoSal = sal * 1.15

print(f'Quem ganhava R${sal:.2f} agora ganha R${novoSal:.2f}')
