valor = float(input('Valor da compra R$ '))
escolha = int(input('''Forma de pagamento:
[1] À vista no dinheiro/cheque
[2] À vista no cartão
[3] Em 2x no cartão
[4] 3x ou mais no cartão
Escolha: '''))

if escolha == 1:
	total = valor * 0.9
	print(f'O Valor final da compra com 10% de desconto é de R${total:.2f}')
elif escolha == 2:
	total = valor * 0.95
	print(f'O valor final da compra com 5% de desconto é de R${total:.2f}')
elif escolha == 3:
	parcelas = valor / 2
	print(f'O valor final da compra com 2 parcelas de R${parcelas:.2f} é de R${valor:.2f}')
elif escolha == 4:
	nParcelas = int(input('Número de parcelas: '))
	total = valor * 1.2
	parcelas = total / nParcelas
	print(f'O valor final da compra com 20% de juros e {nParcelas} parcelas de R${parcelas:.2f} é de R${total:.2f}')
else:
	print('Escolha inválida')
