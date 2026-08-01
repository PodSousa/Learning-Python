print(f'calcular área de trapézio')

base_maior = float(input(f'digite o comprimento da base maior: '))
base_menor = float(input(f'digite o comprimento da base menor: '))
altura = float(input(f'digite o comprimento da altura: '))

if base_maior <= 0 or base_menor <= 0 or altura <= 0:
    print(f'valor de base ou altura inválido')
else: 
    if base_maior > base_menor:
        área = altura * (base_maior + base_menor) / 2
        print(f'a área do trapézio é {área}')
    else:
        print(f'o comprimento da base maior é menor ou igual que da base menor!')
        print(f'base maior = {base_maior}\nbase menor = {base_menor}')
