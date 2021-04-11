import ex107moedas

p = float(input('Digite um preço: R$ '))
print(f'A metade de {p:.2f} é {ex107moedas.metade(p):.2f}.')
print(f'O dobro de {p:.2f} é {ex107moedas.dobro(p):.2f}.')
print(f'Aumentando 10%, temos {ex107moedas.aumentar10(p):.2f}')
print(f'Reduzindo 13%, temos {ex107moedas.diminuir13(p):.2f}')