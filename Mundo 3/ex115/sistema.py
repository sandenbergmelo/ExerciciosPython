from time import sleep
from lib.interface import *
from lib.cadastro import *
from rich import print


def sair():
    """Sai do sistema"""
    print('[red]Saindo do sistema...[/] [green]Até logo.[/]')
    sleep(1)
    exit()


arquivo = 'cadastro.txt'

if not arquivo_existe(arquivo):
    if not criar_arquivo(arquivo):
        print('[red]ERRO com a criação do arquivo[/]')
        sair()

while True:
    resposta = menu([
        'Ver pessoas cadastradas',
        'Cadastrar nova Pessoa',
        'Sair do sistema'
    ])

    if resposta == 1:
        # Opção de listar pessoas cadastradas no sistema
        ver_pessoas(arquivo)
    elif resposta == 2:
        # Opção de cadastrar nova pessoa
        cabeçalho('NOVO CADASTRO')

        nome = input_nome('Nome: ')
        idade = input_int('Idade: ')

        cadastrar_pessoa(arquivo, nome, idade)
    elif resposta == 3:
        sair()
    else:
        print('[red][bold]ERRO![/] Digite uma opção válida![/]')

    sleep(2)
