def resumo(valor=0, aumento=10, redução=5):
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


def aumentar(valor=0, taxa=0, formatar=False):
    """Retorna o valor com uma aumento percentual"""
    res = valor * (100 + taxa) / 100
    if formatar:
        return formatar_moeda(res)
    return res


def reduzir(valor=0, taxa=0, formatar=False):
    """Retorna o valor com uma redução percentual"""
    res = valor * (100 - taxa) / 100
    if formatar:
        return formatar_moeda(res)
    return res


def dobro(valor=0, formatar=False):
    """Retorna o dobro de um valor"""
    res = valor * 2
    if formatar:
        return formatar_moeda(res)
    return res


def metade(valor=0, formatar=False):
    """Retorna a metade de um valor"""
    res = valor / 2
    if formatar:
        return formatar_moeda(res)
    return res


def formatar_moeda(valor=0, moeda='R$'):
    """Formata um valor numérico para um valor monetário"""
    return f'{moeda}{valor:.2f}'.replace('.', ',')
