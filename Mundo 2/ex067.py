# Tabuada 3.0

while True:
    n = int(input('Digite um número: '))

    print('-' * 20)

    if n < 0:
        break

    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
    print('-' * 20)

print('Programa de tabuada encerrado')
