from rich import print


def ler_dinheiro(msg: str = '') -> float:
    """Lê o um número real no formato monetário"""
    while True:
        valor = str(input(msg)).strip().replace(',', '.')

        if valor.isalpha() or valor == '':
            print(f'[red][bold]ERRO![/] \"{valor}\" é um valor inválido![/]')
            continue

        return float(valor)


def ler_int(msg: str = '') -> int:
    """Lê um número inteiro"""
    while True:
        valor = str(input(msg)).strip()

        if not valor.isdigit() or valor == '':
            print('[red][bold]ERRO![/] Digite um número inteiro válido[/]')
            continue

        return int(valor)
