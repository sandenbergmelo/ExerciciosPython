# Unindo dicionários e listas

print('-='*15)
print('Cadastrar pessoas'.center(30))
print('-='*15)

pessoas = []
mulheres = []
soma_das_idades = 0

while True:
    nome = str(input('Nome: ')).strip().title()

    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('ERRO! Responda apenas com M ou F: ')).strip().upper()[0]

    idade = int(input('Idade: '))

    pessoas.append({'nome': nome, 'idade': idade, 'sexo': sexo})

    soma_das_idades += idade

    if sexo == 'F':
        mulheres.append(nome)

    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('ERRO! Responda apenas S ou N: ')).strip().upper()[0]

    print()

    if continuar == 'N':
        break

media_de_idade = soma_das_idades / len(pessoas)

print('-='*20)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media_de_idade:.2f} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}.')
print(f'D) Lista de pessoas que estão acima da média: ')

for pessoa in pessoas:
    if pessoa['idade'] >= media_de_idade:
        print('    ', end='')
        for key, value in pessoa.items():
            print(f'{key} = {value};', end=' ')
        print()
print('<< ENCERRADO >>')
