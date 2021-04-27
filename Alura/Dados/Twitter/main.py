from oo import Requisição

while True:
    opção = str(input('[1] - Fazer Tweet\n[2] - Pesquisar termos\n')).strip()
    if opção == '1' or opção == '2':
        if opção == '1':
            Requisição().cria_requisição('1')
        else:
            Requisição().cria_requisição('2').formata()
    else:
        print('\033[31mOpção inválida, tente novamente!\033[m')

print('\033[34mObrigado por usar o programa!!\003[m')