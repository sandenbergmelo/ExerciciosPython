# Funções para sortear e somar

from random import randint
from time import sleep


def sortear(lista: list):
    print('Sorteando os 5 valores da lista: ', end='')
    for i in range(5):
        lista.append(randint(1, 10))
        print(lista[i], end=' ', flush=True)
        sleep(.3)
    print('Pronto!')


def somar_pares(lista: list):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


valores = []

sortear(valores)
somar_pares(valores)
sortear
