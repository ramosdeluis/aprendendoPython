# -*- encoding: utf-8 -*-
class Url:
    def __init__(self, url):
        self.url = self.limpa_url(url)
        self.valida_url()

    def limpa_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('Erro! A Url está vazia.')

    @property
    def url_base(self):
        indice_interrogacao = self.url.find('?')
        return self.url[:indice_interrogacao]

    def url_parametros(self):
        indice_interrogacao = self.url.find('?')
        return self.url[indice_interrogacao+1:]

    def valor_parametro(self, nome_do_parametro):
        indice_parametro = self.url_parametros().find(nome_do_parametro)
        indice_valor = indice_parametro + len(nome_do_parametro) + 1
        indice_do_e_comercial = self.url_parametros().find('&', indice_valor)
        if indice_do_e_comercial == -1:
            valor = self.url_parametros()[indice_valor:]
        else:
            valor = self.url_parametros()[indice_valor:indice_do_e_comercial]
        return valor

url = Url('https://querodobra.com.br/loja/?filter_product_tag=anime&query_type_product_tag=or')
valor_filter_product_tag = url.valor_parametro('filter_product_tag')
url2 = Url(None)
print(url2)
print(valor_filter_product_tag)