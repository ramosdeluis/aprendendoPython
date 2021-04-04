#n1 = str(input('Digite um número de 0 a 9999.'))
#n2 = '{:0>4}'.format(n1)
#print('Milhar: {}'.format(n2[0]))
#print('Centena: {}'.format(n2[1]))
#print('Dezena: {}'.format(n2[2]))
#print('Unidade: {}'.format(n2[3]))


n1 = int(input('Digite um número de 0 a 9999.'))
m = n1 // 1000 % 10
c = n1 // 100 % 10
d = n1 // 10 % 10
u = n1 // 1 % 10
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))
