from random import shuffle
n1 = input('Nome: ')
n4 = input('Nome: ')
n3 = input('Nome: ')
n2 = input('Nome: ')
l = [n1, n2, n3, n4]
shuffle(l)

print('A ordem de apresentações será: {}'.format(l))
