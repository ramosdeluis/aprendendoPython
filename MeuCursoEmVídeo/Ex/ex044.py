p = float(input('Qual o preço do produto? '))
cp = int(input('''Qual a condição de pagamento:
[1] - À vista em dinheiro/cheque (10% de desconto);
[2] - À vista no cartão (5% de desconto);
[3] - 2 x no cartão (preço normal)
[4] - 3 x ou mais no cartão (20% de juros).
'''))
if 0 < cp <= 4:
    if cp == 1:
        print('O valor normal é R$ {:.2f} e ficará R$ {:.2f} com o desconto de 10%.'.format(p, 0.9*p))
    elif cp == 2:
        print('O valor normal é R$ {:.2f} e ficará R$ {:.2f} com o desconto de 5%.'.format(p, 0.95*p))
    elif cp == 3:
        print('Pagarás o preço normal, de R$ {:.2f}'.format(p))
    else:
        parcelas = int(input('Quantas vezes?'))
        if 2 < parcelas <= 12:
            print('O preço normal de R$ {:.2f} ficará {:.0f}X de R$ {:.2f}, '
                  'totalizando R$ {:.2f}.'.format(p, parcelas, (p*1.2)/parcelas, p*1.2))
        else:
            print('Número de parcelas inválido. Reinicie o programa.')
else:
    print('Opção inválida, reinicie o programa.')


