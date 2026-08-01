número = float(input(f'digite um número: '))

if número >= 0:
	raiz_quadrada = número**(1/2)
	print(f'a raiz quadrada do {número} é {raiz_quadrada}')
else:
	quadrado = número**(2)
	print(f'o {número} ao quadrado é {quadrado}')
