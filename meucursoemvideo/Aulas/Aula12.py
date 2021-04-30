nome = str(input('Qual o teu nome? '))

if nome == 'Luís':
    print('És incrível!')
elif nome == 'Ramos' or nome == 'Alberto':
    print('Que lindo és tu.')
elif nome in 'Carlos Aladiu Bibibi':
    print('És fake.')
else:
    print('Háhá')
print('Que belo nome, tenha um ótimo dia {}'.format(nome))