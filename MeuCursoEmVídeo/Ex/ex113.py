def leiaInt(tex):
        while True:
            v = str(input(tex))
            try:
                int(v)
                return v
            except ValueError:
                print('\033[31mERRO! Digite um número inteiro para continuar.\033[m')
                continue
            except (KeyboardInterrupt):
                print('\033[31mO usuário preferiu não digitar esse número\033[m')
                v = 0
                return v


def leiaReal(tex):
    while True:
        v = str(input(tex)).strip()
        try:
            float(v)
            return v
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar esse número\033[m')
            v = 0
            return v
        except ValueError:
            print('\033[31mERRO! Digite um número real para cuntinuar.\033[m')
            continue




i = leiaInt('Digite um número inteiro: ')
r = leiaReal('Digite um número real: ')
print(f'O número real digitado foi "{r}" e o inteiro foi "{i}".')