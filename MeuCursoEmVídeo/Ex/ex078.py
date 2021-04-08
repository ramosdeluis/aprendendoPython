num = []
for c in range(0, 5):
    num.append(int(input('Digite um valor: ')))
print(f'O maior número digitado foi {max(num)}, que está na posição {num.index(max(num))+1}.')
print(f'O menor número digitado foi {min(num)}, que está na posição {num.index(min(num))+1}.')
