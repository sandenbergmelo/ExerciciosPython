nome = str(input('Digite seu nome completo: ')).strip()
nomeS = nome.split()
n = ''.join(nomeS)

print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome completo tem {len(n)} letras')
print(f'Seu primeiro nome é {nomeS[0]} e ele tem {len(nomeS[0])} letras')
