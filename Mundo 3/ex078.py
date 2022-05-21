valores = []

for i in range(0, 5):
    valores.append(int(input(f'Digite o valor para a posição {i}: ')))

print('=-'*20)

print(f'Você digitou os valores {valores}')

print(f'O menor valor foi {min(valores)} nas posições ', end='')
for i, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{i},', end=' ')
print()

print(f'O maior valor foi {max(valores)} nas posições ', end='')
for i, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{i},', end=' ')
print()
