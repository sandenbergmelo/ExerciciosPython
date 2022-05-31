# Ficha do Jogador

def ficha(nome='<desconhecido>', n_gols='0') -> str:
    """Mostra quantos gols um jogador fez no campeonato

    Keyword Arguments:
        nome {str} -- Nome do jogador (default: {'<desconhecido>'})
        n_gols {str} -- Quantidade de gols (default: {'0'})

    Returns:
        str -- Mensagem com o nome e os gols do jogador
    """

    if nome == '':
        nome = '<desconhecido>'

    if n_gols == '' or not n_gols.isnumeric():
        n_gols = '0'

    return f'O jogador {nome} fez {n_gols} gol(s) no campeonato.'


nome = str(input('Nome do jogador: ')).strip().title()
n_gols = str(input(f'Quantos gols {nome} fez? '))

print(ficha(nome, n_gols))
