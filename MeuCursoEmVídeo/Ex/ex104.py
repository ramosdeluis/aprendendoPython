def leiaInt(str):
    while True:
        nl = input(str)
        if nl.strip() == '' or nl.strip().isnumeric() is False:
            print('\033[31mERRO! Digite um número inteiro.\033[m')
        elif nl.isnumeric():
            n = int(nl)
            return n


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Tu digitaste o número {n}')