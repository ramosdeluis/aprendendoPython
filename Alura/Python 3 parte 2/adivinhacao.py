from random import randint


def jogar():
    maq = randint(0, 100)
    tentativas = 0
    pontos = 1000

    while True:
        dif = int(input('Qual a dificuldade desejada? 1-Fácil, 2-Médio, 3-Difícil: ' ))
        if dif in range(1,4):
            break
        else:
            print('Opção inválida...')
            continue

    if dif == 1:
        tentativas = 15
    elif dif == 2:
        tentativas = 10
    else:
        tentativas = 5

    print('*'*50)
    print(f'{"VAMOS JOGAR!!!":^50}')
    print('*'*50)
    pal = int(input('Tente adivinhar um número entre 0 e 100: '))

    while True:
        if pal == maq:
            break
        else:
            tentativas -= 1
            pontos -= abs(maq - pal)*2
            print(f'Você errou, não é {pal}.', end=' ')
            if pal > maq:
                print(f'O número é menor do que {pal}.')
            else:
                print(f'O número é maior do que {pal}.')
            pal = int(input(f'Digite a {tentativas}ª tentativa: '))

    print('*'*50)
    print('FIM DE JOGO!')
    if pal == maq:
        print('Vocês venceu!')
        print(f'Teu número de pontos foram {pontos}.')
    else:
        print(f'Tu perdeste... todas as {tentativas} tentativas não foram o suficiente...')
    print(f'O número era {maq}.')

if __name__ == '__main__':
    jogar()