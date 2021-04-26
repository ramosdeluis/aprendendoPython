from validate_docbr import CNPJ
from validate_docbr import CPF
import re


class Documento:
    @staticmethod
    def cria_documento(documento):
        for c in '-/,./':
            documento = documento.replace(c, '')
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Número de dígitos inválido!')


class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido!')

    def valida(self, documento):
        validar = CPF()
        return validar.validate(documento)

    def formata(self):
        cpf = CPF()
        return cpf.mask(self.cpf)

    def __str__(self):
        return self.formata()


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido!')

    def valida(self, documento):
        validar = CNPJ()
        return validar.validate(documento)

    def formata(self):
        cnpj = CNPJ()
        return cnpj.mask(self.cnpj)

    def __str__(self):
        return self.formata()


class Telefone:
    def __init__(self, telefone):
        if self.valida(telefone):
            self.telefone = telefone
        else:
            raise ValueError('Telefone inválido!')

    def __str__(self):
        return self.formata()

    def valida(self, telefone):
        padrao = '[+| ]?(\d{2,3})?[ ]?([|(]?\d{2}[)]?)[ ]?(\d{4,5})[-]?(\d{4})'
        if re.findall(padrao, telefone):
            return True
        else:
            return False

    def formata(self):
        padrao = '[+| ]?(\d{2,3})?[ ]?([|(]?\d{2}[)]?)[ ]?(\d{4,5})[-]?(\d{4})'
        resposta = re.search(padrao, self.telefone)
        numero_formatado = f'+{resposta.group(1)} ({resposta.group(2)}) {resposta.group(3)}-{resposta.group(4)}'
        return numero_formatado