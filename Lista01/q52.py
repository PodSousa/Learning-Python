print(f'informe as dimensões do terreno e o preço do metros quadrado de tela')
c = float(input(f'comprimento: '))
l = float(input(f'largura: '))
pmqt = float(input(f'preço do metro quadrado de tela: '))

área = c * l
custo = área / pmqt

print(f'o custo para cercar este mesmo terreno com tela é {custo}')
