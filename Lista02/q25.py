from math import sqrt

a = float(input(f'digite o coefiente a: '))
b = float(input(f'digite o coefiente b: '))
c = float(input(f'digite o coefiente c: '))

if a == 0:
    print(f'não é equação do segundo grau!')
else:
    delta = b*b-4*a*c

    if delta < 0:
        print(f'não existe raiz.')
    elif delta == 0:
        raiz = -b / (2*a)
        print(f'raiz única: {raiz}')
    else:
        raiz1 = (-b + sqrt(delta)) / (2 * a)
        raiz2 = (-b - sqrt(delta)) / (2 * a)
        print(f'primeira raiz: {raiz1}')
        print(f'segunda raiz: {raiz2}')
