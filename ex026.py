frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra a aparece ', frase.count('a'), ' vezes')
print('A primeira letra a apareceu na posição ', frase.find('a') + 1)
print('A primeira letra a apareceu na posição ', frase.rfind('a') + 1)
