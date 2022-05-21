# Times do campeonato brasileiro

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
         'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense',
         'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print('-=' * 30)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 30)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 30)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 30)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
