print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

primeiro = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = int(input('Até que termo? '))
termo = primeiro + termo * r

for i in range(primeiro, termo, r):
	print(i, end=' → ')
print('FIM')
