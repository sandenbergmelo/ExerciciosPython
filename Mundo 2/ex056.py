somaIdade = 0
maiorIdadeHomem = 0
homemVelho = 0
mulheres20 = 0

for i in range(1, 5):
	print(f'----- {i}ª Pessoa -----')
	nome = str(input('Nome: ')).strip()

	idade = int(input('Idade: '))
	somaIdade += idade

	sexo = str(input('Sexo [M/F]: ')).strip().upper()
	if i == 1 and sexo == 'M':
		maiorIdadeHomem = idade
		homemVelho = nome
	if sexo == 'M' and idade > maiorIdadeHomem:
		maiorIdadeHomem = idade
		homemVelho = nome
	if sexo == 'F' and idade < 20:
		mulheres20 += 1

print(f'\nA média de idade do grupo é de {somaIdade / 4:.0f} anos')
print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {homemVelho}')
print(f'Ao todo são {mulheres20} mulheres com menos de 20 anos')
