# Dividindo valores em várias Dividindo valores em várias listas valores em várias listasistas

completa = []
pares = []
impares = []

while True:
    n = int(input('Digite um número: '))

    completa.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]

    if continuar != 'S':
        break

print('-='*18)

print(f'A lista completa é {completa}')
print(f'Os pares são {pares}')
print(f'Os ímpares são {impares}')
