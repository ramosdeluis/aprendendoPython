f = input('Digite uma frase: ').strip()

print('A frase tem {} letras A'.format(f.upper().count('A')))
print('O primeiro a aparece na posição {}'.format(f.upper().find('A')+1))
print('O último a aparece na posição {}'.format(f.upper().rfind('A')+1))
