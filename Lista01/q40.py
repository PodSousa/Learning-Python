número_de_dias_trabalhados = int(input(f'digite o número de dias trabalhados pelo encanador: '))

quantia_líquida = 30 * número_de_dias_trabalhados * (1-8/100)

print(f'quantia líquida a ser paga {quantia_líquida}')
