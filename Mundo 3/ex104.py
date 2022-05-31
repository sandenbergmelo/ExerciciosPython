# Validando entrada de dados em Python

def leia_int(text: str = '') -> int:
    from rich import print

    n = input(text).strip()
    while not n.isnumeric():
        print('[red][bold]ERRO![/] Digite um número inteiro válido[/]')
        n = input(text).strip()

    return int(n)


n = leia_int('Digite um número: ')
print(f'Você digitou o número {n}')
 