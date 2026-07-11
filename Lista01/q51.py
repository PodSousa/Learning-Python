valor_apostador1 = float(input(f'digite o valor do primeiro apostador: '))
valor_apostador2 = float(input(f'digite o valor do segundo apostador: '))
valor_apostador3 = float(input(f'digite o valor do terceiro apostador: '))
prêmio = float(input(f'digite o valor do prêmio: '))

valor_total = valor_apostador1 + valor_apostador2 + valor_apostador3
valor_apostador1 = (valor_apostador1 / valor_total) * prêmio
valor_apostador2 = (valor_apostador2 / valor_total) * prêmio
valor_apostador3 = (valor_apostador3 / valor_total) * prêmio

print(f'parte do prêmio para o primeiro apostador: {valor_apostador1}')
print(f'parte do prêmio para o segundo apostador: {valor_apostador2}')
print(f'parte do prêmio para o terceiro apostador: {valor_apostador3}')
