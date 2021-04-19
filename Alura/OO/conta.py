# -*- encoding: utf-8 -*-
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        valor_disponivel_a_sacar = self.saldo + self.limite
        return valor <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f'O valor de R$ {valor:,.2f} não está disponível para sacar.')

    def extrato(self):
        print(f'O saldo de {self.__titular} é de R$ {self.__saldo:,.2f}')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.title()

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_do_banco():
        return '000'

conta1 = Conta(123, 'Luís', 50, 1000)
conta2 = Conta(321, 'Alberto', 100, 1000)
conta1.transfere(20, conta2)
conta2.extrato()
conta1.extrato()
print(conta1.limite)
conta1.limite = 123456
print(conta1.limite)
print(conta1.saldo)
print(conta1.titular)
Conta.codigo_do_banco()
