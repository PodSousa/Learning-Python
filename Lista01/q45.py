número = int(input(f'digite um número inteiro positivo de 3 dígitos: '))

primeiro = int(número / 100)
segundo = int((número - 100 * primeiro) / 10)
terceiro = número - primeiro * 100 - segundo * 10

print(f'{terceiro}{segundo}{primeiro}')
