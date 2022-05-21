# Valores únicos em uma lista

lista = []

while True:
    n = int(input('Digite um número: '))

    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!\n')
    else:
        print('Valor duplicado! Não foi adicionado!\n')

    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if continuar != 'S':
        break

lista.sort()

print('-='*18)
print(f'Você digitou os valores {lista}')
