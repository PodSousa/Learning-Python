print(f'Escolha a opção:')
print(f'1- Soma de 2 números.')
print(f'2- Diferença entre 2 números (maior pelo menor).')
print(f'3- Produto entre 2 números.')
print(f'4- Divisão entre 2 números (o denominador não pode ser zero).')

opção = int(input(f'Opção '))
A = float(input(f'digite o primeiro número: '))
B = float(input(f'digite o segundo número: '))

if opção == 1:
    print(f'{A} + {B} = {A+B}')
elif opção == 2:
    if A > B:
        print(f'{A} - {B} = {A-B}')
    else:
        print(f'{B} - {A} = {B-A}')
elif opção == 3:
    print(f'{A} * {B} = {A*B}')
elif opção == 4:
    if B != 0:
        print(f'{A} / {B} = {A/B}')
    else:
        print(f'o denominador é zero!')
else:
    print(f'opção inválida')
