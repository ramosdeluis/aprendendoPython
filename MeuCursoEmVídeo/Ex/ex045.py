from random import randint
jogada = int(input('''Faça a tua jogada:
[1] - Pedra;
[2] - Papel;
[3] - Tesoura.
'''))
jogadaMaquina = randint(1,3)
jogadas = ['','Pedra','Papel','Tesoura']

if 0 < jogada < 4:
    if jogada == 1:
        print('A tua jogada foi \033[34m{}\033[m e a da máquina foi \033[33m{}\033[m.'.format(jogadas[jogada], jogadas[jogadaMaquina]))
        if jogada == jogadaMaquina:
            print('EMPATE!')
        elif jogada == 1 and jogadaMaquina == 3:
            print('VENCESTE!')
        elif jogada == 1 and jogadaMaquina == 2:
            print('PERDESTE')
    elif jogada == 2:
        print('A tua jogada foi \033[34m{}\033[m e a da máquina foi \033[33m{}\033[m.'.format(jogadas[jogada], jogadas[jogadaMaquina]))
        if jogada == jogadaMaquina:
            print('EMPATE!')
        elif jogadaMaquina == 3:
            print('PERDESTE!')
        elif jogadaMaquina == 1:
            print('VENCESTE')
    else:
        print('A tua jogada foi \033[34m{}\033[m e a da máquina foi \033[33m{}\033[m.'.format(jogadas[jogada], jogadas[jogadaMaquina]))
        if jogada == jogadaMaquina:
            print('EMPATE!')
        elif jogada == 3 and jogadaMaquina == 2:
            print('VENCESTE!')
        elif jogada == 3 and jogadaMaquina == 1:
            print('PERDESTE')
else:
    print('Jogada inválida. Reinicie o programa.')