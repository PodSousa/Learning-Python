hora_de_trabalho = float(input(f'digite o valor da hora de trabalho em reais: '))
horas_trabalhadas_no_mês = float(input(f'digite o número de horas trabalhadas no mês: '))

valor_a_ser_pago = hora_de_trabalho * horas_trabalhadas_no_mês * (1+10/100)

print(f'valor a ser pago ao funcionário adicionando 10%: {valor_a_ser_pago}')
