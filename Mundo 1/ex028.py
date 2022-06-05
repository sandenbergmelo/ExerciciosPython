import sys, os
from random import randint

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

rand = randint(0, 5)

print('-=-' * 20)
print('Estou pensando em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
n = int(input('Em qual número eu pensei? '))

if n == rand:
	print('PARABÉNS! Você adivinhou!')
else:
	print(f'ERRADO! Eu pensei em {rand}')

input('Pressione enter para jogar outra vez!')
restart_program()
