n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
	print('''	[ 1 ] Somar
	[ 2 ] Multiplicar
	[ 3 ] Maior
	[ 4 ] Novos números
	[ 5 ] Sair do programa''')
	opcao = int(input('Opção: '))

	if opcao == 1:
		soma = n1 + n2
		print(f'\n\n{n1} + {n2} = {soma}\n\n')
	elif opcao == 2:
		produto = n1 * n2
		print(f'\n\n{n1} x {n2} = {produto}\n\n')
	elif opcao == 3:
		maior = max(n1, n2)
		menor = min(n1, n2)
		print(f'\n\n{maior} é maior que {menor}\n\n')
	elif opcao == 4:
		print('Novos números: ')
		n1 = int(input('Primeiro valor: '))
		n2 = int(input('Segundo valor: '))
	elif opcao == 5:
		print('Fim do programa')
	else:
		print('Opção inválida')
	print('=-=' * 10)
else:
	print('Fim do programa')
