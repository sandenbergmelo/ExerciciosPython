n = int(input('Digite um número: '))

u = n % 10 
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 %10

print(f'Unidande: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
