from random import randint
numeroMaquina = randint(0, 10)
contJogadas = 1
lis = ['maior','menor']
print('-=-'*4)
print('VAMOS JOGAR!')
print('-=-'*4)
numeroJogador = int(input('Tente adivinhar o número que a máquina escolheu entre 0 e 10: '))

while numeroJogador != numeroMaquina:
    contJogadas += 1
    if numeroJogador > numeroMaquina:
        numeroJogador = int(input('Jogada errada, o número é {} do que {}. Tente novamente: '.format(lis[1], numeroJogador)))
    else:
        numeroJogador = int(input('Jogada errada, o número é {} do que {}. Tente novamente: '.format(lis[0], numeroJogador)))

print('Você acertou!! O número era \033[34m{}\033[m'.format(numeroMaquina))
print('Você precisou de {} chance (s) para acertar.'.format(contJogadas))
