import random
n1 = input('Nome: ')
n2 = input('Nome: ')
n3 = input('Nome: ')
n4 = input('Nome: ')
r = [n1, n2, n3, n4]

print('O nome sorteado foi: {}'.format(random.choice(r)))
