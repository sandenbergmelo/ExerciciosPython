# Formatando Moedas em Python

from utilidadesCeV import moeda

p = float(input('Digite um preço R$'))

print(f'\nA metade de {moeda.formatar_moeda(p)} é {moeda.formatar_moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.formatar_moeda(p)} é {moeda.formatar_moeda(moeda.dobro(p))}')
print(f'Aumentando 10% temos, {moeda.formatar_moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 10% temos, {moeda.formatar_moeda(moeda.reduzir(p, 10))}')
