# Boletim com listas compostas

from os import system, name

boletim = []

print('-='*15)
print('Cadastrar alunos'.center(30))
print('-='*15)

while True:
    nome = str(input('Nome: ')).strip()
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2

    boletim.append([nome, [nota_1, nota_2], media])

    continuar = str(input('Cadastrar outro aluno? [S/N]: ')).strip().upper()[0]
    print()

    if continuar != 'S':
        break

system('cls' if name == 'nt' else 'clear')

print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)

for i, dados_do_aluno in enumerate(boletim):
    nome = dados_do_aluno[0]
    media = dados_do_aluno[2]

    print(f'{i:<4}{nome:<10}{media:>8.1f}')

while True:
    n_aluno = int(input('\nQuer ver as notas de que aluno? [999 para sair]: '))
    print()

    if n_aluno == 999:
        break

    if n_aluno > len(boletim) - 1 or n_aluno < 0:
        print('Aluno inválido')
        continue

    nome = boletim[n_aluno][0]
    notas = boletim[n_aluno][1]

    print(f'{"Nome":<8}{"Nota 1":^8}{"Nota 2":^8}')
    print('-'*30)
    print(f'{nome:<8}{notas[0]:^8}{notas[1]:^8}')

print('Programa finalizado')
