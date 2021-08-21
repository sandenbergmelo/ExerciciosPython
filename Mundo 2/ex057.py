sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
	sexo = str(input('Dados inválidos. Digite seu sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado')
