from rich import print


def ler_dinheiro(msg: str = '') -> float:
    """Lê o um número real no formato monetário"""
    while True:
        valor = str(input(msg)).strip().replace(',', '.')

        if valor.isalpha() or valor == '':
            print(f'[red][bold]ERRO![/] \"{valor}\" é um valor inválido![/]')
            continue

        return float(valor)


def input_int(msg: str = '') -> int:
    """Lê um número inteiro"""
    while True:
        try:
            valor = int(str(input(msg)).strip())
        except (ValueError, TypeError):
            print('[red][bold]ERRO![/] Digite um número inteiro válido.[/]')
            continue
        except KeyboardInterrupt:
            print('\n[yellow][bold]Interrupção![/] O usuário preferiu interromper a leitura.[/]')
            valor = 0

        return valor


def input_float(msg: str = '') -> float:
    """Lê um número real"""
    while True:
        try:
            valor = float(str(input(msg)).strip().replace(',', '.'))
        except (ValueError, TypeError):
            print('[red][bold]ERRO![/] Digite um número real válido[/]')
            continue
        except KeyboardInterrupt:
            print('\n[yellow][bold]Interrupção![/] O usuário preferiu interromper a leitura.[/]')
            valor = 0.0

        return valor
