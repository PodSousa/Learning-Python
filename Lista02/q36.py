valor_venda = float(input(f'digite o valor da venda: '))

comissão = 0

if valor_venda >= 100000:
    comissão = 700 + valor_venda * 1.16
    
elif 80000 <= valor_venda and valor_venda < 100000:
    comissão = 650 + valor_venda * 1.14
    
elif 60000 <= valor_venda and valor_venda < 80000:
    comissão = 600 + valor_venda * 1.14
    
elif 40000 <= valor_venda and valor_venda < 60000:
    comissão = 550 + valor_venda * 1.14
    
elif 20000 <= valor_venda and valor_venda < 40000:
    comissão = 500 + valor_venda * 1.14

elif 0 <= valor_venda and valor_venda < 20000:
    comissão = 400 + valor_venda * 1.14
else:
    print(f'valor de venda inválido')

if comissão != 0:
    print(f'sua comissão {comissão}')
