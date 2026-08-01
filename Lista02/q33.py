print(f'''
{"PREÇO ANTIGO":<30} {"PERCENTUAL DE AUMENTO":<10}
{"até R$ 50":<30} {"5%":<10}
{"entre R$ 50 e R$ 100":<30} {"10%":<10}
{"acima de R$ 100":<30} {"15%":<10}
''')

preço = float(input(f'digite o preço do produto: '))

if preço < 50:
    preço *= 1.05
elif preço > 100:
    preço *= 1.15
else:
    preço *= 1.10

print(f'\no novo preço é {preço}')

print(f'''
{"PREÇO NOVO":<40} {"MENSAGEM":<10}
{"até R$ 80":<40} {"Barato":<10}
{"entre R$ 80 e R$ 120 (inclusive)":<40} {"Normal":<10}
{"entre R$ 120 e R$ 200 (inclusive)":<40} {"Caro":<10}
{"acima de R$ 200":<40} {"Muito caro":<10}
''')

if preço < 80:
    print(f'barato')
elif 80 <= preço and preço <= 120:
    print(f'normal')
elif preço > 200:
    print(f'muito caro')
else:
    print(f'caro')
