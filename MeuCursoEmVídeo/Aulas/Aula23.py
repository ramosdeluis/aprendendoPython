# Tratamento de Erros e Exceções
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
#except (ValueError, TypeError):
#    print(f'Houve um erro com os tipos de dados digitados.')
#except ZeroDivisionError:
#    print(f'Não é possível dividir por zero.')
#except KeyboardInterrupt:
#    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre! Muito obrigado!')