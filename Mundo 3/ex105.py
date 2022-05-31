# Analisando e gerando Dicionários

def analisar_notas(*notas: float, sit: bool = False) -> dict:
    """Função para analisar notas e situações de vários alunos

    Arguments:
        *notas {float} -- Uma ou mais notas de alunos

    Keyword Arguments:
        sit {bool} -- Se deve ou não adicionar a situação (default: {False})

    Returns:
        dict -- Dicionário com as informações da turma
    """

    infos = {
        'total': len(notas),
        'maior': max(notas),
        'menor': min(notas),
        'média': sum(notas) / len(notas)
    }

    if sit:
        if infos['média'] < 5:
            infos['situação'] = 'RUIM'
        elif infos['média'] < 7:
            infos['situação'] = 'RAZOÁVEL'
        else:
            infos['situação'] = 'BOA'

    return infos


print(analisar_notas(5.5, 7, 6, 10, sit=True))
