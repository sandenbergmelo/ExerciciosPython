# Formatando Moedas em Python

from utilidadesCeV import moeda

p = float(input('Digite um preço R$'))

print(f'\nA metade de {moeda.formatar_moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.formatar_moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% temos, {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13% temos, {moeda.reduzir(p, 13, True)}')
