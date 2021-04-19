# -*- encoding: utf-8 -*-
'''
def cria_conta(numero, titular, saldo, limite):
   conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
   return conta


def deposita(conta, valor):
    conta['saldo'] += valor



def saca(conta, valor):
    conta['saldo'] -= valor


def extrato(conta):
    print(f'O saldo é de R$ {conta["saldo"]:,.2f}.')


conta01 = cria_conta(147, 'Luís', 50000, 1000000)
extrato(conta01)
deposita(conta01, 50000)
extrato(conta01)
saca(conta01, 100000)
extrato(conta01)
'''

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formata(self):
        print(f'{self.dia:0>2}/{self.mes:0>2}/{self.ano:0>4}')

d = Data(21, 11, 2007)
e = Data(0, 0, 1)
e.formata()
d.formata()