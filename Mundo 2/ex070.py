# Estatísticas em produtos

print('-' * 20)
print('Loja'.center(20))
print('-' * 20)

total = 0
produtos_maiores_de_1000 = 0
produto_mais_barato = ''
menor_preco = 0

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    
    total += preco
    if preco > 1000:
        produtos_maiores_de_1000 += 1
    if preco < menor_preco or menor_preco == 0:
        menor_preco = preco
        produto_mais_barato = produto

    print('-' * 20)
    continuar = str(input('Adicionar outro produto? [S/N]: ')).strip().upper()[0]
    print('-' * 20)
    
    if continuar != 'S':
        break

print(f'O total das compras foi R${total:.2f}')
print(f'Temos {produtos_maiores_de_1000} produtos acima de R$1000.00')
print(f'O produto mais barato foi {produto_mais_barato} custando R${menor_preco:.2f}')
