def resumo(valor: float = 0, aumento: float = 10, redução: float = 5) -> None:
    """Mostra um resumo do valor"""
    print('-'*35)
    print('RESUMO DO VALOR'.center(35))
    print('-'*35)

    print(f'Preço analisado: \t{formatar_moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'Aumento de {aumento}%: \t{aumentar(valor, aumento, True)}')
    print(f'Redução de {redução}%: \t\t{reduzir(valor, redução, True)}')

    print('-'*35)


def aumentar(valor: float = 0, taxa: float = 0, formatar: bool = False):
    """Retorna o valor com uma aumento percentual"""
    res = valor * (100 + taxa) / 100
    if formatar:
        return formatar_moeda(res)
    return res


def reduzir(valor: float = 0, taxa: float = 0, formatar: bool = False):
    """Retorna o valor com uma redução percentual"""
    res = valor * (100 - taxa) / 100
    if formatar:
        return formatar_moeda(res)
    return res


def dobro(valor: float = 0, formatar: bool = False):
    """Retorna o dobro de um valor"""
    res = valor * 2
    if formatar:
        return formatar_moeda(res)
    return res


def metade(valor: float = 0, formatar: bool = False):
    """Retorna a metade de um valor"""
    res = valor / 2
    if formatar:
        return formatar_moeda(res)
    return res


def formatar_moeda(valor: float = 0, moeda: str = 'R$') -> str:
    """Formata um valor numérico para um valor monetário"""
    return f'{moeda}{valor:.2f}'.replace('.', ',')
