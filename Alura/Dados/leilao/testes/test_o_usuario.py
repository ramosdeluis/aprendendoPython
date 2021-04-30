
from unittest import TestCase

from alura.dados.leilao.principal.principal import Usuario, Leilao, Lance


class  TestUsuario(TestCase):
    def test_deve_subitrair_da_carteira_o_valor_do_lance():
        usuario = Usuario('Luís', 100)
        leilao = Leilao('Telefone')
        lance = Lance(usuario, 50)
        leilao.adiciona_lance(lance)

        assert usuario.carteira == 50.0

