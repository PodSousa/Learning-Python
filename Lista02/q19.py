número = int(input(f'digite um número inteiro para verificar se é divisível por 3 ou 5: '))

if número % 5 == 0:
    print(f'o número {número} é divisível por 5')
elif número % 3 == 0:
    print(f'o número {número} é divisível por 3')
else:
    print(f'não é divisível por 5 ou 3!')
