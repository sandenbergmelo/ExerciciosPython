# Extraindo dados de uma lista
valores = []

while True:
    valores.append(int(input('Digite um número: ')))

    continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]

    if continuar != 'S':
        break

valores.sort(reverse=True)

print('-='*12)

print(f'Você digitou {len(valores)} valores')
print(f'Os valores em ordem decrescente são {valores}')

if 5 in valores:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
