print(f'informe o horário do início da experiência biológica e a duração, em segundos')

hora = int(input(f'hora: '))
minuto = int(input(f'minuto: '))
segundo = int(input(f'segundo: '))
duração = int(input(f'duração: '))

novo_horário = hora * 3600 + minuto * 60 + segundo + duração

hora_final = novo_horário // 3600
minuto_final = novo_horário % 3600 // 60
segundo_final = novo_horário % 3600 % 60

print(f'\nnovo horário\n\nhora: {hora_final}\nminuto: {minuto_final}\nsegundo: {segundo_final}')
