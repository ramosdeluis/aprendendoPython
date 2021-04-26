import classes
#
# while True:
#     documento = str(input('Digite um documento: '))
#     documento = Documento.cria_documento(documento)
#     print(documento)
#     print('-='*15)
# from classes import Telefone
#
# telefone = Telefone('554833331241')
# print(telefone)
# cadastro = classes.Data()
# print(cadastro)
# print(cadastro.tempo_de_cadastro)
cep = str(input('Digite o teu CEP: 83020'))
cep = classes.Cep(cep)
print(cep)