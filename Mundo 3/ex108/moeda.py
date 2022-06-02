def aumentar(valor=0, taxa=0):
    """Retorna o preço com uma aumento percentual"""
    res = valor * (100 + taxa) / 100
    return res


def diminuir(valor=0, taxa=0):
    """Retorna o preço com uma diminuição percentual"""
    res = valor * (100 - taxa) / 100
    return res


def dobro(valor=0):
    """Retorna o dobro de um preço"""
    res = valor * 2
    return res


def metade(valor=0):
    """Retorna a metade de um preço"""
    res = valor / 2
    return res


def formatar_moeda(valor=0, moeda='R$'):
    """Formata um valor numérico para um valor monetário"""
    res = f'{moeda}{valor:.2f}'.replace('.', ',')
    return res
