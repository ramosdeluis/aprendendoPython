import dominio

luís = dominio.Usuario('Luís')
ramos = dominio.Usuario('Ramos')

lance_ramos = dominio.Lance(ramos, 500)
lance_luís = dominio.Lance(luís, 1000)

leilão = dominio.Leilao('Celular')

# leilão.lances.append(lance_luís)
leilão.lances.append(lance_ramos)
leilão.lances.append(lance_luís)

for lance in leilão.lances:
    print(f'O {lance.usuario.nome} ofereceu R$ {lance.valor:,.2f}')
print('-='*30)
avaliador = dominio.Leiloeiro()
avaliador.avalia(leilão)

print(f'O maior lance foi de R$ {avaliador.maior_valor:,.2f} e o menor foi de R$ {avaliador.menor_valor:,.2f}')