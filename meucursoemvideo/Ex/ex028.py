from random import randint

n1 = randint(0, 5)

n2 = int(input('Tente adivinhar o número aleatório entre 0 e 5: '))

if n1 == n2:
    print('Tu acertaste!! O número era {}'.format(n1))
else:
    print('Tu erraste, o número era {}'.format(n1))
