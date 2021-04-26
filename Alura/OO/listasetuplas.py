from abc import abstractmethod
from functools import total_ordering

@total_ordering
class Conta:
    def __init__(self, codigo, nome, limite):
        self._codigo = codigo
        self._saldo = 0
        self._nome = nome
        self._limite = limite

    def __eq__(self, other):
        if self._saldo != other._saldo:
            return False
        return self._saldo == other._saldo and other._saldo == self._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo

    @property
    def codigo(self):
        return self._codigo

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    @property
    def nome(self):
        return self._nome

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        self._saldo -= valor

    def __str__(self):
        return f'Código: {self.codigo} Nome: {self.nome} Saldo: R$ {self.saldo:,.2f} Limite: {self.limite:,.2f}'

    @abstractmethod
    def passa_o_mes(self):
        pass


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupança(Conta):
    def passa_o_mes(self):
        self._saldo -= 3
        self._saldo *= 1.01


conta1 = Conta(123, 'Luís', 8000)
conta3 = Conta(2, 'Ramos', 1000000)
conta4 = Conta(999, 'Bebeto', 2.79)
print(conta1)
conta1.deposita(55)
conta1.saca(13)
print(conta1)
conta2 = ContaCorrente(278, 'Ramos', 8000)
conta2.deposita(1000)
print(conta2)
conta2.passa_o_mes()
print(conta2)
contas = [conta1, conta2, conta3, conta4]
for conta in contas:
    print(conta, end='-- ')
print()
for conta in sorted(contas, reverse=True):
    print(conta)
print(min(contas))