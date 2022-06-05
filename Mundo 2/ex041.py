from datetime import date

anoAtual = date.today().year
anoNascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = anoAtual - anoNascimento

if idade >= 6:
	if idade <= 9:
		print(f'Com {idade} anos o atleta é MIRIM')
	elif idade <= 14:
		print(f'Com {idade} anos o atleta é INFANTIL')
	elif idade <= 19:
		print(f'Com {idade} anos o atleta é JUNIOR')
	elif idade <= 25:
		print(f'Com {idade} anos o atleta é SÊNIOR')
	else:
		print(f'Com {idade} anos o atleta é MASTER')
else:
	print("Idade Inválida!\nIdade mínima de 6 anos!")
