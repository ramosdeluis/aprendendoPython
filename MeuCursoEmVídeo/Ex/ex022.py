n = input('Qual o teu nome completo? ')

print(n.upper())
print(n.lower())
r = n.split()
print('O nome tem {} letras.'.format(len(''.join(n.split()))))
print('O primeiro nome tem {} letras.'.format(len(r[0])))
