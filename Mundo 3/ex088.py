# Palpites para a Mega Sena

from random import randint
from time import sleep

print('-'*30)
print('JOGAR NA MEGA SENA'.center(30))
print('-'*30)

n = int(input('\nQuantos jogos quer sortear ?: '))

print(f'\n-=-=-= Sorteando {n} Jogos -=-=-=')

for i in range(n):
    numeros = []

    while len(numeros) != 6:
        numero_sorteado = randint(1, 60)

        if numero_sorteado not in numeros:
            numeros.append(numero_sorteado)

    numeros.sort()
    print(f'Jogo {i+1}: {numeros}')
    sleep(1)

print('-=-=-=-=-= Boa Sorte -=-=-=-=-=')
