# Lista ordenada sem o uso de sort()

from rich import print

lista = []

for i in range(0, 5):
    n = int(input('Digite um número: '))

    if i == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Valor {n} adicionado ao final da lista')
    else:
        for j in range(len(lista)):
            if n <= lista[j]:
                lista.insert(j, n)
                print(f'Valor {n} inserido na posição {j}')
                break
print('-='*30)
print(f'Os valores digitados foram {lista}')
