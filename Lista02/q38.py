from datetime import date

dia = int(input(f'digite o seu dia de nascimento: '))
mês = int(input(f'digite o seu mês de nascimento: '))
ano = int(input(f'digite o seu ano de nascimento: '))

if ano < date.today().year:
            
    if 1 <= mês and mês <= 12:
        
        if mês == 4 or mês == 5 or mês == 9 or mês == 11:

            if 1 <= dia and dia <= 30:
               print(f'data válida')
            else:
                print(f'dia inválido')
        else:
            
            if ano % 400 == 0 or (ano % 100 == 0 and ano % 4 != 0):
                if mês == 2 and (1 <= dia and dia <= 29):
                    print(f'data válida')
                else:
                    print(f'dia inválido')
            
            if 1 <= dia and dia <= 31:
               print(f'data válida')
            else:
                print(f'dia inválido')

    else:
        print(f'mês inválido!')

else:
    print(f'ano inválido!')

