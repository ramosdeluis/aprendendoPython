from unittest import TestCase
import dominio


class Leiloeiro(TestCase):
    def setUp(self) -> None:
        self.luís = dominio.Usuario('Luís')
        self.lance_luís = dominio.Lance(self.luís, 1000)
        self.leilão = dominio.Leilao('Celular')
        self.leilão.lances.append(self.lance_luís)

    def test_quando_colocamos_o_menor_lance_primeiro_deve_retornar_o_maior_e_menor_corretamente(self):
        ramos = dominio.Usuario('Ramos')
        lance_ramos = dominio.Lance(ramos, 500)
        self.leilão.lances.append(lance_ramos)
        self.leilão.lances.append(self.lance_luís)

        avaliador = dominio.Leiloeiro()
        avaliador.avalia(self.leilão)

        menor_valor_esperado = 500
        maior_valor_esperado = 1000

        self.assertEqual(menor_valor_esperado, avaliador.menor_valor)
        self.assertEqual(maior_valor_esperado, avaliador.maior_valor)

    def test_quando_colocamos_o_maior_lance_primeiro_deve_retornar_o_maior_e_menor_corretamente(self):
        ramos = dominio.Usuario('Ramos')
        lance_ramos = dominio.Lance(ramos, 500)

        self.leilão.lances.append(self.lance_luís)
        self.leilão.lances.append(lance_ramos)

        avaliador = dominio.Leiloeiro()
        avaliador.avalia(self.leilão)

        menor_valor_esperado = 500
        maior_valor_esperado = 1000

        self.assertEqual(menor_valor_esperado, avaliador.menor_valor)
        self.assertEqual(maior_valor_esperado, avaliador.maior_valor)

    def test_quando_colocamos_somente_um_valor_deve_retornar_maior_e_menor_iguais_ao_mesmo(self):
        self.leilão.lances.append(self.lance_luís)

        avaliador = dominio.Leiloeiro()
        avaliador.avalia(self.leilão)

        menor_valor_esperado = 1000
        maior_valor_esperado = 1000

        self.assertEqual(menor_valor_esperado, avaliador.menor_valor)
        self.assertEqual(maior_valor_esperado, avaliador.maior_valor)

    def test_quando_colocamos_mais_de_dois_valores_deve_retornar_o_maior_e_menor_corretamente(self):
        ramos = dominio.Usuario('Ramos')
        lance_ramos = dominio.Lance(ramos, 500)
        nunes = dominio.Usuario('Ramos')
        lance_nunes = dominio.Lance(ramos, 900)

        self.leilão.lances.append(self.lance_luís)
        self.leilão.lances.append(lance_ramos)
        self.leilão.lances.append(lance_nunes)

        avaliador = dominio.Leiloeiro()
        avaliador.avalia(self.leilão)

        menor_valor_esperado = 500
        maior_valor_esperado = 1000

        self.assertEqual(menor_valor_esperado, avaliador.menor_valor)
        self.assertEqual(maior_valor_esperado, avaliador.maior_valor)
