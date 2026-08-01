import math

hora_chegada = int(input(f'digite a hora de chegada: '))
minuto_chegada = int(input(f'digite o minuto de chegada: '))

hora_partida = int(input(f'digite a hora de partida: '))
minuto_partida = int(input(f'digite o minuto de partida: '))


tempo_minutos = 60 * hora_partida + minuto_partida - (60 * hora_chegada  + minuto_chegada)
tempo_horas = (tempo_minutos // 60) + math.ceil((tempo_minutos % 60) / 60)

if tempo_horas < 0:
    tempo_horas = 25 + tempo_horas
elif tempo_horas == 0:
    tempo_horas = 24


if 1 <= tempo_horas and tempo_horas <= 2:
    tarifa = 1 * tempo_horas
elif 3 <= tempo_horas and tempo_horas <= 4:
    tarifa = 1.40 * tempo_horas
else:
    tarifa = 2 * tempo_horas

print(f'tarifa a pagar {tarifa}')
