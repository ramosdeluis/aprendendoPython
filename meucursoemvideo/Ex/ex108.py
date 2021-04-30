import ex108moedas

p = float(input('Digite o preço: R$ '))
print(f'O dobro de {ex108moedas.moeda(p)} é {ex108moedas.moeda(ex108moedas.dobro(p))}.')
print(f'A metade de {ex108moedas.moeda(p)} é {ex108moedas.moeda(ex108moedas.metade(p))}.')
print(f'Aumentado 10%, temos {ex108moedas.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {ex108moedas.diminuir(p, 13)}')
