# Um print especial

def escreva(msg: str):
    tamanho = len(msg) + 4

    print('~'*tamanho)
    print(msg.center(tamanho))
    print('~'*tamanho)


escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
