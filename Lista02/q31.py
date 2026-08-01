altura = float(input(f'digite a altura: '))
peso = float(input(f'digite o peso: '))

if altura < 1.20:
    if peso < 60:
        print(f'A')
    elif peso > 90:
        print(f'G')
    else:
        print(f'D')
elif altura > 1.70:
    if peso < 60:
        print(f'C')
    elif peso > 90:
        print(f'I')
    else:
        print(f'F')
else:
    if peso < 60:
        print(f'B')
    elif peso > 90:
        print(f'H')
    else:
        print(f'E')
