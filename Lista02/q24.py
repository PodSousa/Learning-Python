valor = float(input(f'digite o valor do produto: '))
estado = input(f'digite o estado(MG, SP, RJ ou MS): ')

if estado == 'MG':
    preço_final = valor * (1+7/100)
    print(f'preço final do produto acrescido do imposto do estado(MG): {preço_final}')
elif estado == 'SP':
    preço_final = valor * (1+12/100)
    print(f'preço final do produto acrescido do imposto do estado(SP): {preço_final}')
elif estado == 'RJ':
    preço_final = valor * (1+15/100)
    print(f'preço final do produto acrescido do imposto do estado(RJ): {preço_final}')
elif estado == 'MS':
    preço_final = valor * (1+8/100)
    print(f'preço final do produto acrescido do imposto do estado(MS): {preço_final}')
else:
    print(f'estado não identificado')
