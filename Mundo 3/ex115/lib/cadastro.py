from lib.interface import cabeçalho


def arquivo_existe(arquivo: str) -> bool:
    try:
        with open(arquivo, 'r'):
            pass
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(arquivo: str) -> bool:
    try:
        with open(arquivo, 'w+'):
            pass
    except Exception:
        return False
    else:
        return True


def ver_pessoas(arquivo: str) -> None:
    try:
        cabeçalho('PESSOAS CADASTRADAS')

        with open(arquivo, 'r') as cadastros:
            for linha in cadastros:
                dados = linha.split(';')

                nome = dados[0]
                idade = dados[1].replace('\n', '')

                print(f'{nome:<30} {idade:>3} anos')

    except Exception:
        print('ERRO')


def cadastrar_pessoa(arquivo: str,
                     nome: str = 'desconhecido', idade: int = 0) -> None:
    from rich import print

    try:
        with open(arquivo, 'a+') as cadastros:
            cadastros.write(f'{nome};{idade}\n')
    except:
        print('[red]Erro ao cadastrar pessoa.[/]')
    else:
        print(f'Novo registro de {nome} adicionado com [green]sucesso[/].')
