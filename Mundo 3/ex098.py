# Função de Contador

from time import sleep


def contador(inicio: int, fim: int, passo: int):
    print('-='*15)

    if passo < 0:
        passo *= (-1)
    if passo == 0:
        passo = 1

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2)

    if inicio < fim:
        for c in range(inicio, fim+1, passo):
            print(c, end=' ', flush=True)
            sleep(.5)
        print('FIM!')
    else:
        for c in range(inicio, fim-1, -passo):
            print(c, end=' ', flush=True)
            sleep(.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('-='*15)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
