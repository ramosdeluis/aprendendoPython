n = int(input('Escreva um número inteiro: '))
o = int(input('''Escolha uma das opções:
[1] converter para Binário;
[2] coverter para Octal;
[3] converter para Hexadecimal.
'''))
if o == 1 or o == 2 or o == 3:
    if o == 1:
        print('{} em binário é igual a {}'.format(n, bin(n)[2:]))
    elif o == 2:
        print('{} em octal é igual a {}'.format(n, oct(n)[2:]))
    else:
        print('{} em hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('''Opção inválida, reinicie o programa.''')

