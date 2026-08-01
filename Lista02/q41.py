peso = float(input(f'digite o seu peso: '))
altura = float(input(f'digite a sua altura: '))

imc = peso / altura**2

if imc < 18.5:
    print(f'abaixo do peso')
elif 18.6 <= imc and imc <= 24.9:
    print(f'saudável')
elif 25.0 <= imc and imc <= 29.9:
    print(f'peso em excesso')
elif 30.0 <= imc and imc <= 34.9:
    print(f'obesidade grau 1')
elif 35.0 <= imc and imc <= 39.9:
    print(f'obesidade grau 2(severa)')
else:
    print(f'obesidade grau 3(mórbida)')
