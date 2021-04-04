print('=-='*20)
print('Olá, vamos calcular o valor de empréstimo de uma casa!!')
print('=-='*20)

v = float(input('Quanto custa a casa? '))
s = float(input('Qual o teu salário? '))
a = float(input('Em quantos anos pretendes pagar o imóvel? '))
parcela = v/(a * 12)
if 0.3 * s >= parcela:
    print('O empréstimo foi aprovado!')
    print('O valor da parcela será de R$ {:.2f}'.format(parcela))
    print('O valor será pago em {:.0f} meses, sem juros.'.format(12*a))
else:
    print('Empréstimo negado... o teu salário não é suficiente para pagar a parcela do imóvel.')
    print('O valor o teu salário precisa ser R$ {:.2f} para arcar com R$ {:.0f} em {} meses.'.format(parcela/0.3, v, 12*a))
