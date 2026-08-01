trabalho_laboratório = float(input(f'digite a nota do trabalho de laboratório: '))
avaliação_semestral = float(input(f'digite a nota da avaliação semestral: '))
exame_final = float(input(f'digite a nota do exame final: '))


if 10 > trabalho_laboratório and trabalho_laboratório > 0:
    if 10 > avaliação_semestral and avaliação_semestral > 0:
        if 10 > exame_final and exame_final > 0:
            
            média = (2*trabalho_laboratório + 3*avaliação_semestral + 5*exame_final) / 10
            
            print(f'sua média é {média}')
            
            if 2.9 >= média and média >= 0:
                print(f'reprovado!')
            elif 4.9 >= média and média >= 3:
                print(f'recuperação!')
            else:
                print(f'aprovado!')
                
        else:
            print(f'nota do exame final fora do intervalo [0:10]')
    else:
        print(f'nota da avaliação semestral fora do intervalo [0:10]')
else:
    print(f'nota do trabalho de laboratório fora do intervalo [0:10]')
