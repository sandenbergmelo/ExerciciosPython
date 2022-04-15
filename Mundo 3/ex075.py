# Análise de tuplas

valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite outro número: ')))


print(f'\nVocê digitou os valores: {valores}')

print(f'O valor 9 apareceu {valores.count(9)} vezes')

if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição')

print(f'Os valores pares são: ', end='')
for valor in valores:
    if valor % 2 == 0:
        print(valor, end=' ')
