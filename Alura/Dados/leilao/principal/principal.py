from sys import float_info


class Usuario:

    def __init__(self, nome, carteira=0):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_valor = float_info.min
        self.menor_valor = float_info.max

    def adiciona_lance(self, lance: Lance):
        if not self.__lances or self.__lances[-1].usuario != lance.usuario and self.__lances[-1].valor < lance.valor:
            if self.maior_valor < lance.valor:
                self.maior_valor = lance.valor
            if self.menor_valor > lance.valor:
                self.menor_valor = lance.valor

            self.__lances.append(lance)
        else:
            raise ValueError('Lance inválido!')

    @property
    def lances(self):
        return self.__lances[:]
