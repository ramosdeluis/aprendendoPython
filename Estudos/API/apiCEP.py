# Aprendendo a usar API de CEP
import requests


def main():
    print('-'*20)
    print(f'{"Consultando CEP":^20}')
    print('-'*20)

    cep_input = str(input('Digite o teu CEP: '))

    if len(cep_input) != 8:
        print('\033[31mCEP Inválida! Reinicie o Programa.\033[m')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    addres_data = request.json()

    if 'erro' not in addres_data:
        print('\033[33m===> CEP ENCONTRADO <===\033[m')
        print(f'CEP: {addres_data["cep"]}')
        print(f'Logradouro: {addres_data["logradouro"]}')
        print(f'Bairro: {addres_data["bairro"]}')
        print(f'Cidade: {addres_data["localidade"]}')
        print(f'Estado: {addres_data["uf"]}')
        print(f'DDD: {addres_data["ddd"]}')
    else:
        print(f'\033[31m{cep_input} é um CEP Inválida! Reinicie o Programa.\033[m ')

if __name__ == '__main__':
    while True:
        main()
        while True:
            cont = str(input('Queres digitar outro CEP? [S/N] ')).strip().upper()
            if cont in 'SN':
                break
        if cont in 'N':
            break

print('\nObrigado por usar o programa! \nVolte sempre!')