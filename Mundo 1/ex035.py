print('-=' * 12)
print('Analisando triângulos')
print('-=' * 12)
print('\n')

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
	print('Os seguimentos informados formam um triângulo')
else:
	print('Os seguimentos informados não formam um triângulo')
