from math import sqrt

print(f'digite os valores dos catetos')

a = float(input(f'digite o valor do cateto a: '))
b = float(input(f'digite o valor do cateto b: '))

hipotenusa = sqrt(a**2 + b**2)

print(f'o valor da hipotenusa é {hipotenusa}')
