# Mais matrizes em Python

from rich import print

matriz = [[], [], []]

soma_dos_pares = 0
soma_da_terceira_coluna = 0

for i in range(3):
    for j in range(3):
        n = int(input(f'Digite um valor para a posição [{i}, {j}]: '))
        matriz[i].append(n)

        if n % 2 == 0:
            soma_dos_pares += n

        if j == 2:
            soma_da_terceira_coluna += n

print()

for linha in matriz:
    for valor in linha:
        print(f'[ {valor:^5} ]', end=' ')
    print()

print()

print(f'A soma dos valores pares é igual a {soma_dos_pares}')
print(f'A soma dos valores da terceira coluna é igual a {soma_da_terceira_coluna}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
