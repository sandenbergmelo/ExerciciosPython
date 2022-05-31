# Funções para votação

def voto(nascimento: int) -> str:
    """Função para verificar se uma
    pessoa precisa votar

    Args:
        nascimento (int): Ano de nascimento

    Returns:
        str: Mensagem personalizada com o resultado
    """

    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - nascimento

    msg = f'Com {idade} anos: '

    if idade < 16:
        msg += 'NÃO VOTA.'
    elif idade < 18 or idade > 65:
        msg += 'VOTO OPCIONAL.'
    else:
        msg += 'VOTO OBRIGATÓRIO.'

    return msg


print('-'*30)
nascimento = int(input('Em que ano você nasceu? '))

print(voto(nascimento))
