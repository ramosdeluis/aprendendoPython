from validate_docbr import CPF


class Cpf:
    def __init__(self, cpf):
        if self.cpf_e_valido(cpf):
            self._cpf = self.cpf_e_valido(cpf)
        else:
            raise ValueError('CPF Inválido')

    def __str__(self):
        return self.formata_cpf()

    # def valida_numericamente(self):
    #     cpf = self._cpf
    #     soma1 = 0
    #     soma2 = 0
    #     cont = 10
    #     for numero in cpf[:-2]:
    #         aqui = int(numero) * cont
    #         soma1 += aqui
    #         cont -= 1
    #     print(11-(soma1%11))
    #     cont = 11
    #     for numero in cpf[:-1]:
    #         aqui = int(numero) * cont
    #         soma2 += aqui
    #         cont -= 1
    #     print(11-(soma2%11))

    def cpf_e_valido(self, cpf):
        valida_cpd = CPF()
        cpf = cpf.replace('-', '')
        cpf = cpf.replace('.', '')
        if valida_cpd.validate(cpf):
            return cpf
        raise ValueError('CPF Inválido!!')
        # cpf = cpf.replace('-', '')
        # cpf = cpf.replace('.', '')
        # if len(cpf.strip()) == 11:
        #     return cpf
        # else:
        #     return False

    def formata_cpf(self):
        cpf = CPF()
        return cpf.mask(self._cpf)
        # cpf = self._cpf
        # return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'