# Jogo de par ou impar

from random import randint
from rich import print

print('=-' * 10)
print('Jogo de Par ou Impar')
print('=-' * 10)

vitorias = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    
    total = jogador + computador

    palpite = 'x'
    while palpite not in 'pi':
        palpite = str(input('Par ou Impar [P/I]: ').lower().strip()[0])
    
    print('=-' * 10)

    print(f'Você jogou {jogador} e o computador jogou {computador}')
    print(f'Total de {total}')

    if total % 2 == 0:
        print(f'Deu Par!')
        print('=-' * 10)

        if palpite == 'p':
            print('Você [green]VENCEU![/]')
            print('=-' * 10)
            vitorias += 1
        else:
            break
    else:
        print(f'Deu Impar!')
        print('=-' * 10)

        if palpite == 'i':
            print('Você [green]VENCEU![/]')
            print('=-' * 10)
            vitorias += 1
        else:
            break
    print('Vamos jogar de novo')


print('Você [red]PERDEU![/]')
print('[red]GAME OVER[/]')
print(f'Total de vitórias: {vitorias}')
print('=-' * 10)
