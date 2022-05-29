# Aprimorando os Dicionários

from os import system, name

print('-='*16)
print('Cadastro de Jogadores de Futebol')
print('-='*16)

time = []

while True:
    nome = str(input('Nome: ')).strip().title()
    n_de_partidas = int(input(f'Quantas partidas {nome} jogou? '))

    gols = []
    for partida in range(n_de_partidas):
        gols.append(int(input(f'    Quantos gols na partida {partida+1}? ')))

    time.append({'nome': nome, 'gols': gols, 'total': sum(gols)})

    continuar = str(input('Cadastrar outro jogador? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('ERRO! Digite apenas S ou N: ')).strip().upper()[0]

    print()

    if continuar == 'N':
        break

system('cls' if name == 'nt' else 'clear')

print(f'  {"Nº":<3}{"Nome":<15}{"Gols":<25}{"Total":<5}')
print('-'*52)

for partida, jogador in enumerate(time):
    nome = jogador['nome']
    gols = jogador['gols']
    total = jogador['total']

    print(f'  {partida:<3}{nome:<15}{str(gols):<25}{total:<5}')

print('-'*52)

while True:
    n_jogador = int(input('Quer ver os dados de qual jogador? [999 encerra]: '))

    if n_jogador == 999:
        break

    if n_jogador >= len(time) or n_jogador < 0:
        print(f'\nERRO! Não existe jogador com o código {n_jogador}')
        continue

    jogador = time[n_jogador]

    print(f'\n-- Levantamento do jogador {jogador["nome"]} --')
    for partida, n_gols in enumerate(jogador['gols']):
        print(f'  Na partida {partida+1} fez {n_gols} gols')
    print('-'*52)

print('<< ENCERRADO >>')
