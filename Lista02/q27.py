idade = int(input(f'digite a idade do nadador: '))

if 5 <= idade and idade <= 7:
    print(f'infantil A')
elif 8 <= idade and idade <= 10:
    print(f'infantil B')
elif 11 <= idade and idade <= 13:
    print(f'juvenil A')
elif 14 <= idade and idade <= 17:
    print(f'juvenil B')
elif idade >= 18:
    print(f'sênior')
else:
    print(f'é só um bebezinho')
