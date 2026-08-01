número = int(input(f'digite um número inteiro maior que zero com 3 dígitos: '))

if número > 0:
	terceiro = número // 100
	segundo = (número - terceiro * 100) // 10
	primeiro =  número - terceiro * 100 - segundo * 10
	soma = primeiro + segundo + terceiro
	print(f'a soma dos dígitos é {soma}')
else:
	print(f'número inválido!')
