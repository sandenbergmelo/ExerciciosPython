# Função que calcula área

def calcular_area(largura, comprimento):
    area = largura * comprimento
    print(f'\nA área de um terreno {largura}x{comprimento} é de {area}m².')


print(' Controle de Terrenos')
print('-'*22)

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

calcular_area(largura, comprimento)
