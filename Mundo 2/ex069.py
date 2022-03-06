# Análise de dados do grupo

maiores_de_18 = 0
homens = 0
mulheres_menores_de_20 = 0

while True:
    print('-' * 30)
    print('Cadastrar uma pessoa'.center(30))
    print('-' * 30)

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        maiores_de_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menores_de_20 += 1
    
    print('-' * 30)
    continuar = str(input('Quer continuar?: [S/N]: ')).strip().upper()[0]

    if continuar != 'S':
        break

print('-'*30)
print(f'Total de pessoas maiores de 18 anos: {maiores_de_18}')
print(f'Temos {homens} homens cadastrados')
print(f'E temos {mulheres_menores_de_20} mulheres com menos de 20 anos')
