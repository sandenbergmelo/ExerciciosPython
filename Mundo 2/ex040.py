n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

m = (n1 + n2) / 2
print(f'Média: {m:.1f}')

if m < 5:
	print(f'Aluno Reprovado!')
elif m < 7:
	print(f'Aluno em recuperação!')
else:
	print(f'Aluno Aprovado!')
