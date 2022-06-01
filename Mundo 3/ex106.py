# Sistema interativo de ajuda em Python

from time import sleep


def título(text: str, cor: str = 'white', cor_back: str = '') -> None:
    from rich import print

    tamanho = len(text) + 4

    print(f'[{cor}][on {cor_back}]~[/][/]' * tamanho)
    print(f'[{cor}][on {cor_back}][bold]  {text}  [/][/][/]')
    print(f'[{cor}][on {cor_back}]~[/][/]' * tamanho)


def ajuda(comando: str) -> None:
    from rich import print

    título(
        f'Acessando o manual do comando \'{comando}\'', cor='white', cor_back='#10568f')
    sleep(1)

    try:
        print(f'[on white][black]{eval(comando).__doc__}[/][/]')
    except (SyntaxError, NameError):
        print(f'O comando \'{comando}\' não foi reconhecido')

    sleep(1)


while True:
    título('SISTEMA DE AJUDA PyHELP', cor_back='#148f10')
    sleep(1)
    comando = str(input('Comando, Função ou Biblioteca > ')).strip().lower()

    if comando == 'fim' or comando == 'sair':
        break

    ajuda(comando)

título('ATÉ LOGO!', cor_back='red')
sleep(1)
