nota = float(input(f'digite a nota: '))
faltas = int(input(f'digite o número de faltas: '))

if faltas <= 20:
    if 9 <= nota and nota <= 10:
        print(f'CONTEITO A')
    elif 7.5 <= nota and nota <= 8.9:
        print(f'CONTEITO B')
    elif 5.0 <= nota and nota <= 7.4:
        print(f'CONTEITO C')
    elif 4.0 <= nota and nota <= 4.9:
        print(f'CONTEITO D')
    elif 0 <= nota and nota <= 3.9:
        print(f'CONTEITO E')
    else:
        print(f'nota inválida')
else:
    if 9 <= nota and nota <= 10:
        print(f'CONTEITO B')
    elif 7.5 <= nota and nota <= 8.9:
        print(f'CONTEITO C')
    elif 5.0 <= nota and nota <= 7.4:
        print(f'CONTEITO D')
    elif 4.0 <= nota and nota <= 4.9:
        print(f'CONTEITO E')
    elif 0 <= nota and nota <= 3.9:
        print(f'CONTEITO F')
    else:
        print(f'nota inválida')
