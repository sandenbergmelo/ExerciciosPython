def aumentar(preço, taxa):
    """Retorna o número com uma aumento percentual"""
    res = preço * (100 + taxa) / 100
    return res


def diminuir(preço, taxa):
    """Retorna o número com uma diminuição percentual"""
    res = preço * (100 - taxa) / 100
    return res


def dobro(preço):
    """Retorna o dobro de um número"""
    res = preço * 2
    return res


def metade(preço):
    """Retorna a metade de um número"""
    res = preço / 2
    return res
