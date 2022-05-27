# Jogo de Dados em Python

from operator import itemgetter
from random import randint
from time import sleep

resultados = {}

quantidade = int(input('Quantidade de jogadores: '))

for i in range(quantidade):
    resultados[f'Jogador{i+1}'] = randint(1, 6)

print('\nResultados: ')

for key, value in resultados.items():
    print(f'{key} tirou {value} no dado.')
    sleep(1)

ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)

print('\n ===== Ranking dos jogadores ===== ')
for i, resultado in enumerate(ranking):
    print(f'  {i+1}º Lugar: {resultado[0]} com {resultado[1]} pontos.')
    sleep(1)
