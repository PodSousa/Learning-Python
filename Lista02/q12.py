from math import log10

número = int(input(f'digite um número inteiro: '))

if número > 0:
	logaritmo = log10(número)
	print(f'o logaritmo de {número} é {logaritmo}')
else:
	print(f'número inválido!')
