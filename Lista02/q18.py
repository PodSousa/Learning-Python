print(f'calculadora 2026!\n')
print(f'opções de operações:')
print(f'SOMA(digite 1)\nSUBTRAÇÃO(digite 2)\nMULTIPLICAÇÃO(digite 3)\nDIVISÃO(digite 4)\n')

opção = int(input(f'digite sua opção: '))
A = float(input(f'digite o valor de A: '))
B = float(input(f'digite o valor de B: '))

print(f'')

if opção == 1:
 print(f'{A} + {B} = {A+B}')   
elif opção == 2:
    print(f'{A} - {B} = {A-B}')
elif opção == 3:
    print(f'{A} * {B} = {A*B}')
elif opção == 4:
    print(f'{A} / {B} = {A/B}')
else:
    print(f'opção inválida!')
