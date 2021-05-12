reais = float(input('Digite em valor em reais R$'))

# Cotação das moedas no dia 12/05/2021
dolar = 5.3
euro = 6.4

print(f'R${reais:.2f} valem US${reais/dolar:.2f}')
print(f'R${reais:.2f} valem €{reais/euro:.2f}')
