ano = int(input(f'digite o ano: '))

if ano % 400 == 0 or (ano % 4 == 0 and not(ano % 100 == 0)):
    print(f'é ano bissexo')
else:
    print(f'não é ano bissexto')
