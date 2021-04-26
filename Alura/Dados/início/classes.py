from validate_docbr import CNPJ
from validate_docbr import CPF
from datetime import datetime, timedelta
import requests
import locale
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


class Data():
    def __init__(self):
        self.momento_de_cadastro = datetime.today()

    def __str__(self):
        return self.formata()

    def mes_de_cadastro(self):
        meses = ['janeiro', 'fevereiro', 'março',
                 'abril', 'maio', 'junho', 'julho',
                 'agosto', 'setembro', 'outubro',
                 'novembro', 'dezembrp']
        mes_atual = self.momento_de_cadastro.month
        return meses[mes_atual-1]

    def dia_do_mes_do_cadastro(self):
        return self.momento_de_cadastro.day

    def dia_da_semana_no_cadastro(self):
        dias = ['segunda-feira', 'terça-feira',
                'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
        dia = self.momento_de_cadastro.weekday()
        return dias[dia]

    def formata(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR')
        return self.momento_de_cadastro.strftime('%A - %d/%m/%Y - %H:%M').title()
        # return f'Cadastro: \n{"Dia:":<6}{self.dia_do_mes_do_cadastro():} ({self.dia_da_semana_no_cadastro().title()}) ' \
        #        f'\n{"Mês:":<6}{self.mes_de_cadastro().title()} ' \
        #        f'\n{"Ano:":<6}{self.momento_de_cadastro.year}' \
        #        f'\n{"Hora:":<6}{self.momento_de_cadastro.hour}:{self.momento_de_cadastro.minute}'

    @property
    def tempo_de_cadastro(self):
        return datetime.today() - (self.momento_de_cadastro + timedelta(days=50, hours=25))


class Cep():
    def __init__(self, cep):
        if self.valida_cep(cep):
            self.cep = cep
            self.url = f'http://viacep.com.br/ws/{cep}/json/'
            self.info = self.solicita_cep()
        else:
            raise ValueError('\033[33mCEP Inválido!\033[m')

    def __str__(self):
        return self.formata_cep()

    def valida_cep(self, cep):
        if len(str(cep)) == 8:
            return True
        else:
            return False

    def formata_cep(self):
        return f'{"CEP:":<8}{self.info["cep"]}' \
               f'\n{"Rua:":<8}{self.info["logradouro"]}'\
               f'\nBairro: {self.info["bairro"]}'\
               f'\nCidade: {self.info["localidade"]}'\
               f'\nEstado: {self.info["uf"]}'

    def solicita_cep(self):
        r = requests.get(self.url)
        return r.json()