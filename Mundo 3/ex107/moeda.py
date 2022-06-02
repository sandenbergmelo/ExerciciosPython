def aumentar(preço, taxa):
    """Retorna o preço com uma aumento percentual"""
    res = preço * (100 + taxa) / 100
    return res


def diminuir(preço, taxa):
    """Retorna o preço com uma diminuição percentual"""
    res = preço * (100 - taxa) / 100
    return res


def dobro(preço):
    """Retorna o dobro de um preço"""
    res = preço * 2
    return res


def metade(preço):
    """Retorna a metade de um preço"""
    res = preço / 2
    return res
