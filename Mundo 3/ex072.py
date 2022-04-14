# Números por extenso

numeros_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro',
                       'cinco', 'seis', 'sete', 'oito', 'nove',
                       'dez', 'onze', 'doze', 'treze', 'quatorze',
                       'quinze', 'dezesseis', 'dezessete', 'dezoito',
                       'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))

    if 0 <= n <= 20:
        print(f'\nVocê digitou o número {numeros_por_extenso[n]}')
    else:
        print('\nTente novamente.')
        continue

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar != 'S':
        break
