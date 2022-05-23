# Validando expressões matemáticas

ex = input('Digite uma expressão: ')

parenteses = []

for simbolo in ex:
    if simbolo == '(':
        parenteses.append('(')
    if simbolo == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break

if len(parenteses) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')
