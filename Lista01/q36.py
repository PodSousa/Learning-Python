from math import pi

altura = float(input(f'digite a altura do cilindro: '))
raio = float(input(f'digite o raio do cilindro: '))

volume = pi * raio**2 * altura

print(f'o volume do cilindro é {volume:.3f}')
