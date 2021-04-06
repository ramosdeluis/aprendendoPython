op = 1.5
while op != 5 and 6 > op > 0:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    op = int(input('''O que desejas fazer?
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos Números
[5] - Sair do programa
'''))
    if op == 1:
        print('A soma de \033[32m{}\033[m com \033[33m{}\033[m é \033[34m{}\033[m.'.format(n1, n2, n1+n2))
        op = 5
    if op == 2:
        print('O produto de \033[32m{}\033[m com \033[33m{}\033[m é \033[34m{}\033[m.'.format(n1, n2, n1 * n2))
        op = 5
    if op == 3:
        if n1 > n2:
            print('\033[33m{}\033[m é maior do que \033[34m{}\033[m.'.format(n1, n2))
            op = 5
        elif n2 > n1:
            print('\033[33m{}\033[m é maior do que \033[34m{}\033[m.'.format(n2, n1))
            op = 5
        else:
            print('Os números \033[34m{}\033[m e \033[34m{}\033[m são iguais.'.format(n1, n2))
if op == 5:
    print('FIM')
else:
    print('Opção inválida, reinicie o programa.')
