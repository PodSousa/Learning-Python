salário = float(input(f'digite o seu salário: '))
tempo_serviço = int(input(f'digite o seu tempo de serviço: '))

if salário <= 500:
    novo_salário = salário * 1.25
elif salário <= 1000:
    novo_salário = salário * 1.20
elif salário <= 1500:
    novo_salário = salário * 1.15
elif salário <= 2000:
    novo_salário = salário * 1.1
else:
    novo_salário = salário

if 1 <= tempo_serviço and tempo_serviço <= 3:
    novo_salário += 100
elif 4 <= tempo_serviço and tempo_serviço <= 6:
    novo_salário += 200
elif 7 <= tempo_serviço and tempo_serviço <= 10:
    novo_salário += 300
elif tempo_serviço > 10:
    novo_salário += 500

print(f'novo salário: {novo_salário}')
