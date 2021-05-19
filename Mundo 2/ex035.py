casa = float(input('Valor da casa R$'))
sal = float(input('Salário do comprador R$'))
anos = int(input('Quantos anos de financiamento? '))

valorParcelas = casa / (anos * 12)
print(f'Para o financiamento dessa cassa de R${casa:.2f} em {anos} anos\no valor da parcela será de R${valorParcelas:.2f}')

if (sal * 0.3) >= valorParcelas:
	print('Empréstimo pode ser CONCEDIDO!')
else:
	print('Empréstimo NEGADO!')
