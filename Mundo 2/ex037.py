n = int(input('Digite um número: '))

escolha = int(input('''Escolha uma base para converter o número
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal
Opção: '''))

if escolha == 1:
	print(f'O número {n} em binário é {n:b}')
elif escolha == 2:
	print(f'O número {n} em octal é {n:o}')
elif escolha == 3:
	print(f'O número {n} em exadecimal é {n:x}')
else:
	print('Escolha INVÁLIDA!')
