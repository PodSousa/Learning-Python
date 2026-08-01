nota1 = float(input(f'digite a primeira nota: '))
nota2 = float(input(f'digite a segunda nota: '))

if 10.0 >= nota1 and nota1 >= 0.0 and 10.0 >= nota2 and nota2 >= 0.0:
	média = (nota1 + nota2) / 2
	print(f'a média das notas é {média}')
else:
	print(f'notas inválidas!')
