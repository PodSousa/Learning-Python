dia = int(input(f'digite o dia: '))
mês = int(input(f'digite o mês: '))
ano = int(input(f'digite o ano: '))

if ano >= 1:
    if 1 <= mês and mês <= 12:
        if mês == 1:
            if 1 <= dia and dia <= 31:
                print(f'data: {dia} de janeiro de {ano}')
        elif mês == 2:
            if 1 <= dia and dia <= 28:
                print(f'data: {dia} de fevereiro de {ano}')
            if ano % 400 == 0 or (ano % 100 == 0 and ano % 4 != 0):
                if 1 <= dia and dia <= 29:
                    print(f'data: {dia} de fevereiro de {ano}')
        elif mês == 3:
            if 1 <= dia and dia <= 31:
                print(f'data: {dia} de março de {ano}')
        elif mês == 4:
            if 1 <= dia and dia <= 30:
                print(f'data: {dia} de abril de {ano}')
        elif mês == 5:
            if 1 <= dia and dia <= 30:
                print(f'data: {dia} de maio de {ano}')
        elif mês == 6:
            if 1 <= dia and dia <= 30:
                print(f'data: {dia} de junho de {ano}')
        elif mês == 7:
            if 1 <= dia and dia <= 31:
                print(f'data: {dia} de julho de {ano}')
        elif mês == 8:
            if 1 <= dia and dia <= 31:
                print(f'data: {dia} de agosto de {ano}')
        elif mês == 9:
            if 1 <= dia and dia <= 30:
                print(f'data: {dia} de setembro de {ano}')
        elif mês == 10:
            if 1 <= dia and dia <= 31:
                print(f'data: {dia} de outubro de {ano}')
        elif mês == 11:
            if 1 <= dia and dia <= 30:
                print(f'data: {dia} de novembro de {ano}')
        else:
            if 1 <= dia and dia <= 31:
                print(f'data: {dia} de dezembro de {ano}')
    else:
        print(f'mês inválido')
else:
    print(f'ano inválido')



    
