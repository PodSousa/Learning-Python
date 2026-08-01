ladoA = float(input(f'digite o comprimento do lado A do triângulo: '))
ladoB = float(input(f'digite o comprimento do lado B do triângulo: '))
ladoC = float(input(f'digite o comprimento do lado C do triângulo: '))

if ladoA < (ladoB + ladoC) and ladoB < (ladoA + ladoC) and ladoC < (ladoA + ladoB):
    if ladoA == ladoB and ladoA == ladoC:
        print(f'é um triângulo equilátero')
    elif ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
        print(f'é um triângulo escaleno')
    else:
        print(f'é um triângo isósceles')
else:
    print(f'esse lados não compoem um triângulo!')
