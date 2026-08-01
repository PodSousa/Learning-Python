número = float(input(f'digite um número para calcularmos a raiz quadrada: '))

if número >=0:
	raiz_quadrada = número**0.5
	print(f'a raiz quadrada do {número} é {raiz_quadrada}')
else:
	print(f'números negativos não possuem raiz quadrada!')
