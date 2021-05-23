s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if (s1 < s2 + s3) and (s2 < s1 + s3) and (s3 < s1 + s2):
	if s1 == s2 == s3:
		print('Os segmentos inseridos formam um triângulo equilátero!')
	elif s1 != s2 != s3 != s1:
		print('Os segmentos inseridos formam um triângulo escaleno')
	else:
		print('Os segmentos inseridos formam um triângulo isósceles')
else:
	print('Os segmentos inseridos não formam um triângulo.')
