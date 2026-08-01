salário = float(input(f'digite o salário de um trabalhador: '))
prestação_empréstimo = float(input(f'digite o valor da prestação de um empréstimo: '))

if prestação_empréstimo / salário > (20/100):
	print(f'empréstimo não concedido!')
else:
	print(f'empréstimo concedido!')
