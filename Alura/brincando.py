class Moeda:
    @staticmethod
    def gera_moeda(código, valor):
        if código == 1:
            return EuroReal(valor)
        elif código == 2:
            return RealEuro(valor)


class RealEuro:
    def __init__(self, valor):
        self.valor = valor
        self.valor_convertido = self.converte()

    def __str__(self):
        return self.formata()

    def converte(self):
        valor_convertido = self.valor / 6.56
        return valor_convertido

    def formata(self):
        return f'R$ {self.valor:,.2f} = € {self.valor_convertido:,.2f}'\
            .replace(',', '_').replace('.',',').replace('_','.')


class EuroReal:
    def __init__(self, valor):
        self.valor = valor
        self.valor_convertido = self.converte()

    def __str__(self):
        return self.formata()

    def converte(self):
        valor_convertido = self.valor * 6.56
        return valor_convertido

    def formata(self):
        return f'€ {self.valor:,.2f} = R$ {self.valor_convertido:,.2f}'\
            .replace(',', '_').replace('.',',').replace('_','.')



euros = Moeda.gera_moeda(1, 90000000)
reais = Moeda.gera_moeda(2, 1200000)
print(reais)
print(euros)