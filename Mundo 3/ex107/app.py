# Exercitando módulos em Python

import moeda

p = float(input('Digite um preço R$'))

print(f'\nA metade de {p} é R${moeda.metade(p)}')
print(f'O dobro de {p} é R${moeda.dobro(p)}')
print(f'Aumentando 10% temos, R${moeda.aumentar(p, 10)}')
print(f'Diminuindo 10% temos, R${moeda.diminuir(p, 10)}')
