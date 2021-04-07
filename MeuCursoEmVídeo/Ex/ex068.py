from random import randint
maquina = randint(0, 99)
vitorias = 0
op = ['par', 'ímpar']
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-'*15)
while True:
    jogador = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] '))
    soma = jogador + maquina
    if soma % 2 == 0 and escolha in 'Pp':
        vitorias += 1
    elif soma % 2 != 0 and escolha in 'Ii':
        vitorias += 1
    else:
        break
    print('=-' * 15)
    print('Tu venceste! Jogando novamente...')
    print('=-' * 15)
print(f'A maquina escolheu \033[34m{maquina}\033[m e tu \033[33m{jogador}\033[m. O total deu \033[31m{soma}\033[m, {op[soma%2]}.')
print('=-'*15)
print('Tu PERDESTE!')
print('=-'*15)
print(f'FIM DE JOGO! Tu venceste {vitorias} vezes.')
