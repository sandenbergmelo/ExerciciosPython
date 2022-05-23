# Listas com pares e ímpares

valores = [[], []]

for i in range(1, 8):
    n = int(input(f'Digite o {i}º número: '))

    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

valores[0].sort()
valores[1].sort()

print(f'\nOs valores pares foram {valores[0]}')
print(f'Os valores ímpares foram {valores[1]}')
