from datetime import date
anoAtual = date.today().year

anoNascimento = int(input('Ano de nascimento: '))
idade = anoAtual - anoNascimento
print(f'Quem nasceu em {anoNascimento} tem {idade} anos em {anoAtual}.')

if idade < 18:
	print(f'Faltam {18 - idade} anos para se alistar.')
	print(f'Alistamento em {anoAtual + (18 - idade)}')
elif idade > 18:
	print(f'Já deveria ter se alistado há {idade - 18} anos.')
	print(f'O alistamento foi em {anoAtual - (idade - 18)}.')
elif idade == 18:
	print("Deve se alistar imediatamente!")
