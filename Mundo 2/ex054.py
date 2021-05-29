from datetime import date
anoAtual = date.today().year
maior = 0
menor = 0

quantidade = int(input('Analisar quantas pessoas? '))

for i in range(1, quantidade + 1):
	anoNasc = int(input(f'Em que ano nasceu a {i}ª pessoa? '))
	if anoAtual - anoNasc >= 18:
		maior += 1
	else:
		menor += 1

print(f'\n{maior} pessoas maiores de idade')
print(f'{menor} pessoas menores de idade')
