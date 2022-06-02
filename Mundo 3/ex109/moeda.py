def aumentar(valor=0, taxa=0, formatar=False):
    """Retorna o preço com uma aumento percentual"""
    res = valor * (100 + taxa) / 100
    if formatar:
        return formatar_moeda(res)
    return res


def diminuir(valor=0, taxa=0, formatar=False):
    """Retorna o preço com uma diminuição percentual"""
    res = valor * (100 - taxa) / 100
    if formatar:
        return formatar_moeda(res)
    return res


def dobro(valor=0, formatar=False):
    """Retorna o dobro de um preço"""
    res = valor * 2
    if formatar:
        return formatar_moeda(res)
    return res


def metade(valor=0, formatar=False):
    """Retorna a metade de um preço"""
    res = valor / 2
    if formatar:
        return formatar_moeda(res)
    return res


def formatar_moeda(valor=0, moeda='R$'):
    """Formata um valor numérico para um valor monetário"""
    return f'{moeda}{valor:.2f}'.replace('.', ',')
