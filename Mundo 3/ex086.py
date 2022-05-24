# Matriz em Python

from rich import print

matriz = [[], [], []]

for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite um valor para a posição [{i}, {j}]: ')))

print()

for linha in matriz:
    for valor in linha:
        print(f'[ {valor:^5} ]', end=' ')
    print()
