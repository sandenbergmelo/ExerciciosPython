# Função para Fatorial

def fatorial(x: int, show: bool = False) -> str:
    """Calcula o fatorial de um número.

    Arguments:
        x {int} -- O número a ser calculado.

    Keyword Arguments:
        show {bool} -- Mostrar ou não a conta. (default: {False})

    Returns:
        str -- O valor do fatorial com ou sem conta
        de acordo com o parâmetro show
    """

    f = 1
    calculo = ''

    for i in range(x, 0, -1):
        f *= i

        if i > 1:
            calculo += f'{i} x '
        else:
            calculo += f'{i} = {f}'

    if show:
        return calculo

    return f


n = int(input('Digite um número: '))

print(fatorial(n, show=True))
