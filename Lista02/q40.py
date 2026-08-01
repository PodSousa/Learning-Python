fábrica = float(input(f'digite o preço de fábrica: '))

if fábrica < 12000:
    distribuidor = 1.05
    impostos = 1
elif 12000 <= fábrica and fábrica <= 25000:
    distribuidor = 1.10
    impostos = 1.15
else:
    distribuidor = 1.15
    impostos = 1.20

consumir = fábrica * distribuidor * impostos

print(f'o custo ao consumidor: {consumir}')
