# Função que descobre o maior

from time import sleep


def maior(*valores):
    print('-='*20)
    print('Analisando os valores passados...')

    for valor in valores:
        print(valor, end=' ', flush=True)
        sleep(.3)
    print(f'\nForam informados {len(valores)} valores ao todo.')

    maior_valor = 0 if len(valores) == 0 else max(valores)

    print(f'O maior valor informado foi {maior_valor}')


maior(2, 9, 4, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
