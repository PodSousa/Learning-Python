nota1 = float(input(f'digite a nota da primeira prova: '))
nota2 = float(input(f'digite a nota da segunda prova: '))
nota3 = float(input(f'digite a nota da terceira prova: '))

média_ponderada = (nota1 * 1 + nota2 * 1 + nota3 * 2) / 4

if média_ponderada >= 60:
	print(f'aprovado com média ponderada igual a {média_ponderada}')
else:
	print(f'reprovado com média ponderada igual a {média_ponderada}')
