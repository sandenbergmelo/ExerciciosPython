# Caixa Eletrônico

print('=' * 20)
print('Banco'.center(20))
print('=' * 20)

valor = int(input('Valor que deseja sacar: R$'))

total = valor

cedulas_de_50 = 0
cedulas_de_20 = 0
cedulas_de_10 = 0
cedulas_de_1 = 0

while total >= 50:
    total -= 50
    cedulas_de_50 += 1
while total >= 20:
    total -= 20
    cedulas_de_20 += 1
while total >= 10:
    total -= 10
    cedulas_de_10 += 1
while total >= 1:
    total -= 1
    cedulas_de_1 += 1

print('=' * 20)
print('Total de:')

if cedulas_de_50 > 0:
    print(f'{cedulas_de_50} cedulas de R$50')
if cedulas_de_20 > 0:
    print(f'{cedulas_de_20} cedulas de R$20')
if cedulas_de_10 > 0:
    print(f'{cedulas_de_10} cedulas de R$10')
if cedulas_de_1 > 0:
    print(f'{cedulas_de_1} cedulas de R$1')

print('=' * 20)
