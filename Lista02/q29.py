import random

print(f'provinha')

acertos = 0

a1 = random.randint(1, 100)
b1 = random.randint(1, 100)
r1 = int(input(f'qual é a soma de {a1} + {b1}? '))
if a1 + b1 == r1:
    print(f'acertou')
    acertos += 1
else:
    print(f'errou, a resposta certa é {a1+b1}')


a2 = random.randint(1, 100)
b2 = random.randint(1, 100)
r2 = int(input(f'qual é a soma de {a2} + {b2}? '))
if a2 + b2 == r2:
    print(f'acertou')
    acertos += 1
else:
    print(f'errou, a resposta certa é {a2+b2}')

a3 = random.randint(1, 100)
b3 = random.randint(1, 100)
r3 = int(input(f'qual é a soma de {a3} + {b3}? '))
if a3 + b3 == r3:
    print(f'acertou')
    acertos += 1
else:
    print(f'errou, a resposta certa é {a3+b3}')

a4 = random.randint(1, 100)
b4 = random.randint(1, 100)
r4 = int(input(f'qual é a soma de {a4} + {b4}? '))
if a4 + b4 == r4:
    print(f'acertou')
    acertos += 1
else:
    print(f'errou, a resposta certa é {a4+b4}')

a5 = random.randint(1, 100)
b5 = random.randint(1, 100)
r5 = int(input(f'qual é a soma de {a5} + {b5}? '))
if a5 + b5 == r5:
    print(f'acertou')
    acertos += 1
else:
    print(f'errou, a resposta certa é {a5+b5}')

print(f'acertou {acertos} perguntas, continue sempre estudando =D')

