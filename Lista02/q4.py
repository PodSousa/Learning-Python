número = float(input(f'digite um número: '))

if número >= 0:
	quadrado = número**(2)
	raiz_quadrada = número**(1/2)
	print(f'o {número} ao quadrado é {quadrado}')
	print(f'a raiz quadrada do {número} é {raiz_quadrada}')
else:
	print(f'o número é negativo!')
