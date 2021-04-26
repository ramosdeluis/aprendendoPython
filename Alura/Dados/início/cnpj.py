from validate_docbr import CNPJ
class Cnpj:
    def __init__(self, cnpj):
        if self.valida_cnpj(cnpj):
            self._cnpj = self.valida_cnpj(cnpj)
        else:
            raise ValueError('CNPJ Inválido!!')

    def valida_cnpj(self, cnpj):
        validar = CNPJ()
        cnpj = cnpj.replace('-', '')
        cnpj = cnpj.replace('.', '')
        cnpj = cnpj.replace('/', '')
        if validar.validate(cnpj):
            return cnpj

    def __str__(self):
        return self.formata_cnpj()

    def formata_cnpj(self):
        cnpj = CNPJ()
        return cnpj.mask(self._cnpj)

