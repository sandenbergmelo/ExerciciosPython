# Sorteio de números em tupla
from random import randint

valores = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Valores sorteados: {valores}')

print(f'O maior valor foi {max(valores)}')
print(f'O menor valor foi {min(valores)}')
