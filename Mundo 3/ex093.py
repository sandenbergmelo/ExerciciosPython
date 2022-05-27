# Cadastro de Jogador de Futebol

print('-='*15)
print('Cadastro de Jogador de Futebol')
print('-='*15)

jogador = {}

jogador['nome'] = str(input('Nome: ')).strip().title()
n_de_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

jogador['gols'] = []
for partida in range(n_de_partidas):
    jogador['gols'].append(int(input(f'    Quantos gols na partida {partida+1}? ')))

jogador['total'] = sum(jogador['gols'])

print()

print('-='*30)
print(jogador)
print('-='*30)

print()

for key, value in jogador.items():
    print(f'{key}: {value}')

print(f'\nO jogador {jogador["nome"]} jogou {n_de_partidas} partidas.')

for partida, gols in enumerate(jogador['gols']):
    print(f'    => Na partida, {partida+1} marcou {gols} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
