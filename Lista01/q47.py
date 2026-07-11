segundos = int(input(f'digite um valor inteiro em segundos: '))

horas = segundos // 3600
minutos = segundos % 3600 // 60
segundos = segundos % 3600 % 60

print(f'horas: {horas}\nminutos: {minutos}\nsegundos: {segundos}')
