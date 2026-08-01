distância = float(input(f'digite a distância em km: '))
quantidade_gasolina = float(input(f'digite a quantidade de litros de gasolina consumidos por um carro em um percurso: '))

consumo = distância / quantidade_gasolina

if consumo < 8:
    print(f'venda o carro!')
elif consumo > 14:
    print(f'super econômico!')
else:
    print(f'econômico!')
