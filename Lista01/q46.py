número = int(input(f'digite um número inteiro de 4 dígitos (de 1000 a 9999): '))

milhar = int(número / 1000)
centena = int((número - milhar * 1000) / 100)
dezena = int((número - milhar * 1000 - centena * 100) / 10)
unidade = número - milhar * 1000 - centena * 100 - dezena * 10 

print(f'milhar: {milhar}')
print(f'centena: {centena}')
print(f'dezena: {dezena}')
print(f'unidade: {unidade}')
