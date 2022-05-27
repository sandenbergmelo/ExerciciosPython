# Cadastro de Trabalhador em Python

from datetime import date
ano_atual = date.today().year

trabalhador = {}

print('-='*15)
print('Informações do trabalhador'.center(30))
print('-='*15)

trabalhador['nome'] = str(input('Nome: ')).strip().title()
nascimento = int(input('Ano de nascimento: '))
trabalhador['idade'] = ano_atual - nascimento
trabalhador['cpts'] = int(input('Carteira de trabalho [0 = não tem]: '))

if trabalhador['cpts'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = (trabalhador['contratação'] - nascimento) + 35

print()

for key, value in trabalhador.items():
    print(f' - {key}: {value}')
