altura = float(input(f'digite sua altura: '))
sexo = input(f'digite o seu sexo(homem ou mulher): ')

if sexo == 'homem':
	peso_ideal = (72.7 * altura) - 58
	print(f'seu peso ideal é {peso_ideal}')
elif sexo == 'mulher':
	peso_ideal = (62.1 * altura) - 44.7
	print(f'seu peso ideal é {peso_ideal}')
else:
	print(f'sexo não identificado, digite homem ou mulher.')

