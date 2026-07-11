altura_do_degrau = float(input(f'informe a altura do degrau de uma escada: '))
altura_a_alcançar = float(input(f'informe a altura que o usuário deseja alcançar subindo a escada: '))

quantidade_de_degraus = round(altura_a_alcançar / altura_do_degrau)

print(f'são {quantidade_de_degraus} degraus para que o usuário deverá subir para atingir seu objetivo!')
