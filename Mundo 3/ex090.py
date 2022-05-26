# Dicionário em Python

aluno = {}

print('-='*15)
print('Cadastrar aluno'.center(30))
print('-='*15)

aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print()
for key, value in aluno.items():
    print(f'{key} => {value}')
