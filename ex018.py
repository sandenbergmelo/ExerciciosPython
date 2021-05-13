from math import sin, cos, tan, radians

an = float(input('Digite o valor do ângulo: '))
seno = sin(radians(an))
coss = cos(radians(an))
tang = tan(radians(an))

print(f'O seno de {an} é {seno:.2f}')
print(f'O cosseno de {an} é {coss:.2f}')
print(f'A tângente de {an} é {tang:.2f}')
