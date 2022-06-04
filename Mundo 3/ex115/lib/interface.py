from rich import print


def input_int(msg: str = '') -> int:
    """Lê um número inteiro"""
    while True:
        try:
            valor = int(str(input(msg)).strip())
        except (ValueError, TypeError):
            print('[red][bold]ERRO![/] Digite um número inteiro válido.[/]')
            continue
        except KeyboardInterrupt:
            print(
                '\n[yellow][bold]Interrupção![/] O usuário preferiu interromper a leitura.[/]')
            valor = 0

        return valor


def input_nome(msg: str = '') -> str:
    while True:
        try:
            nome = str(str(input(msg)).strip())
            if nome == '':
                print('[red][bold]ERRO![/] Digite um nome.[/]')
                continue
        except (ValueError, TypeError):
            print('[red][bold]ERRO![/] Digite um nome.[/]')
            continue
        except KeyboardInterrupt:
            print('[red][bold]ERRO![/] Digite um nome .[/]')
            continue

        return nome

def linha(tamanho: int = 42) -> str:
    return '-' * tamanho


def cabeçalho(txt: str) -> str:
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista: list) -> int:
    cabeçalho('MENU PRINCIPAL')

    for i, item in enumerate(lista):
        print(f'[yellow]{i+1}[/] - [blue]{item}[/]')
    print(linha())

    opc = input_int('Sua opção: ')
    return opc
