from random import randint


def jogar():
    cabecalho()
    resultado(jogando(escolhendo_categoria()), palavra_secreta)


def cabecalho():
    print('*'*30)
    print(f'{"VAMOS JOGAR FORCA!":^30}')
    print('*'*30)


def escolhendo_categoria():
    escolha_lista = int(input('Qual categoria queres jogar? \n[1] - Frutas\n[2] - Verbos\n[3] - Nomes \n'))
    if escolha_lista == 1:
        palavras = open('frutas.txt', 'r')
        escolha_lista = []
        escolha_lista.clear()
        print(f'É uma Fruta: ')
        for linha in palavras:
            linha = linha.strip()
            escolha_lista.append(linha)
        palavras.close()
    if escolha_lista == 2:
        palavras = open('verbos.txt', 'r')
        escolha_lista = []
        escolha_lista.clear()
        print(f'É um verbo: ')
        for linha in palavras:
            linha = linha.strip()
            escolha_lista.append(linha)
        palavras.close()
    if escolha_lista == 3:
        palavras = open('nomes.txt', 'r')
        escolha_lista = []
        escolha_lista.clear()
        print(f'É um nome: ')
        for linha in palavras:
            linha = linha.strip()
            escolha_lista.append(linha)
        palavras.close()
    return escolha_lista


def jogando(lis):
    acertou = False
    perdeu = False
    erros = 0
    global palavra_secreta
    palavra_secreta = lis[randint(0, len(lis) - 1)].upper()
    palavra_escondida = ['_' for letra in palavra_secreta]

    while not acertou and not perdeu:
        print(palavra_escondida)
        chute = str(input('Digite o teu chute: ')).strip().upper()
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if letra == chute:
                    palavra_escondida[index] = chute
                index += 1
        else:
            erros += 1
            desenha_forca(erros)
        perdeu = erros == 7
        acertou = '_' not in palavra_escondida
    print(palavra_escondida)
    l = []
    l.append(acertou)
    l.append(perdeu)
    return l


def resultado(l, palavra_secreta):
    if l[0]:
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    if l[1]:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == '__main__':
    jogar()
