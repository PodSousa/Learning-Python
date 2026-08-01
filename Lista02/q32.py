print(f'e aí bora lanchar!?')

print(f'''
{"Especificação":<20} {"Código":<8} {"Preço":<5}
{"Cachorro Quente":<20} {"100":<8} {"1.20":<5}
{"Bauru Simples":<20} {"101":<8} {"1.30":<5}
{"Bauru com Ovo":<20} {"102":<8} {"1.50":<5}
{"Hamburguer":<20} {"103":<8} {"1.20":<5}
{"Cheeseburguer":<20} {"104":<8} {"1.70":<5}
{"Suco":<20} {"105":<8} {"2.20":<5}
{"Refrigerante":<20} {"106":<8} {"1.00":<5}
''')

código = int(input(f'o que você vai querer(digite o código)? '))
quantidade = int(input(f'vai querer quantos? '))

preço = 0

if código == 100:
    preço = 1.20
elif código == 101:
    preço = 1.30
elif código == 102:
    preço = 1.50
elif código == 103:
    preço = 1.20
elif código == 104:
    preço = 1.70
elif código == 105:
    preço = 2.20
elif código == 106:
    preço = 1.00
else:
    print(f'produto não identificado')

if preço != 0:
    preço *= quantidade
    print(f'vai ficar {preço}')
