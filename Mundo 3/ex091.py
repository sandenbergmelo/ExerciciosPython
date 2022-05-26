# Jogo de Dados em Python

from operator import itemgetter
from random import randint
from time import sleep

resultados = {
    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(1, 6),
    'Jogador4': randint(1, 6),
}

print('Resultados: ')

for key, value in resultados.items():
    print(f'{key} tirou {value} no dado.')
    sleep(1)

ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)

print('\n ===== Ranking dos jogadores ===== ')
for i, resultado in enumerate(ranking):
    print(f'  {i+1}º Lugar: {resultado[0]} com {resultado[1]} pontos.')
    sleep(1)
