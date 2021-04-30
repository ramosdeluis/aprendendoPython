from alura.dados.leilao.principal.principal import Usuario, Leilao, Lance
from unittest import TestCase


class Leiloeiro(TestCase):
    def setUp(self) -> None:
        self.luís = Usuario('Luís')
        self.lance_luís = Lance(self.luís, 1000)
        self.leilão = Leilao('Celular')


    def test_quando_colocamos_o_menor_lance_primeiro_deve_retornar_o_maior_e_menor_corretamente(self):
        ramos = Usuario('Ramos')
        lance_ramos = Lance(ramos, 500)
        self.leilão.adiciona_lance(lance_ramos)
        self.leilão.adiciona_lance(self.lance_luís)

        menor_valor_esperado = 500
        maior_valor_esperado = 1000

        self.assertEqual(menor_valor_esperado, self.leilão.menor_valor)
        self.assertEqual(maior_valor_esperado, self.leilão.maior_valor)

    def test_nao_deve_érmitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(ValueError):
            ramos = Usuario('Ramos')
            lance_ramos = Lance(ramos, 500)
            self.leilão.adiciona_lance(self.lance_luís)
            self.leilão.adiciona_lance(lance_ramos)

    def test_quando_colocamos_somente_um_valor_deve_retornar_maior_e_menor_iguais_ao_mesmo(self):
        self.leilão.adiciona_lance(self.lance_luís)

        menor_valor_esperado = 1000
        maior_valor_esperado = 1000

        self.assertEqual(menor_valor_esperado, self.leilão.menor_valor)
        self.assertEqual(maior_valor_esperado, self.leilão.maior_valor)

    def test_quando_colocamos_mais_de_dois_valores_deve_retornar_o_maior_e_menor_corretamente(self):
        ramos = Usuario('Ramos')
        nunes = Usuario('Nunes')
        lance_nunes = Lance(nunes, 900)
        lance_ramos = Lance(ramos, 500)
        self.leilão.adiciona_lance(lance_ramos)
        self.leilão.adiciona_lance(lance_nunes)
        self.leilão.adiciona_lance(self.lance_luís)


        menor_valor_esperado = 500
        maior_valor_esperado = 1000

        self.assertEqual(menor_valor_esperado, self.leilão.menor_valor)
        self.assertEqual(maior_valor_esperado, self.leilão.maior_valor)


    def test_se_o_ultimo_usuario_for_o_mesmo_nao_deve_permitir_dar_um_lance(self):
        with self.assertRaises(ValueError):
            self.leilão.adiciona_lance(self.lance_luís)
            self.leilão.adiciona_lance(self.lance_luís)

    def test_se_o_valor_for_maior_do_que_o_maior_deve_adicionar(self):
        ramos = Usuario('Ramos')
        lance_ramos = Lance(ramos, 2000)
        self.leilão.adiciona_lance(self.lance_luís)
        self.leilão.adiciona_lance(lance_ramos)

        quantidade_de_lances = len(self.leilão.lances)

        self.assertEqual(2, quantidade_de_lances)

    def test_se_o_valor_for_menor_do_que_o_maior_nao_deve_adicionar(self):
        with self.assertRaises(ValueError):
            ramos = Usuario('Ramos')
            lance_ramos = Lance(ramos, 500)
            self.leilão.adiciona_lance(self.lance_luís)
            self.leilão.adiciona_lance(lance_ramos)
