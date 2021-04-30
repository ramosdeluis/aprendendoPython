'''Listas Compostas'''

teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
galera.append(teste)
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
l1 = []
g1 = []
l1.append('Ramos')
l1.append(22)
g1.append(l1[:])
l1[0] = 'Luís'
l1[1] = 1.73
g1.append(l1)
print(g1)
'''
galera = [['Luís', 12], ['Alberto', 22], ['Ramos', 32], ['Nunes', 42]]
for pe in galera:
    #print(f'{pe[0]} tem {pe[1]} anos de idade.')
    if pe[1] >= 21:
        print(f'{pe[0]} tem {pe[1]}, logo, é maior de idade.')
'''