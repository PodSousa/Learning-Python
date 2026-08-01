x = float(input(f'digite o valor x: '))
y = float(input(f'digite o valor y: '))
z = float(input(f'digite o valor z: '))

geométrica = (x * y * z)**(1/3)
ponderada = (x + 2*y + 3*z) / 6
harmônica = 1 / ((1/x) + (1/y) + (1/z))
aritmética = (x + y + z) / 3

print(f'média geométrica: {geométrica}')
print(f'média ponderada: {ponderada}')
print(f'média harmônica: {harmônica}')
print(f'média aritmética: {aritmética}')
