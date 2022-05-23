# Lista composta e análise de dados

from rich import print

pessoas = []
dados = []
mais_leves = []
mais_pesadas = []
maior_peso = menor_peso = total_de_pessoas = 0

while True:
    print('Cadastrar pessoa: ')
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    total_de_pessoas += 1

    continuar = str(input('Cadastrar nova pessoa? [S/N]: ')).strip().upper()[0]
    print()

    if continuar != 'S':
        break

for i, pessoa in enumerate(pessoas):
    if i == 0:
        menor_peso = maior_peso = pessoa[1]
    elif pessoa[1] > maior_peso:
        maior_peso = pessoa[1]
    elif pessoa[1] < menor_peso:
        menor_peso = pessoa[1]

for pessoa in pessoas:
    if pessoa[1] == menor_peso:
        mais_leves.append(pessoa[0])
    elif pessoa[1] == maior_peso:
        mais_pesadas.append(pessoa[0])

print(f'Ao todo foram cadastradas {total_de_pessoas} pessoas')
print(f'O menor peso foi {menor_peso}Kg. Peso de {mais_leves}')
print(f'O maior peso foi {maior_peso}Kg. Peso de {mais_pesadas}')
