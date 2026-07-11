valor_total = float(input(f'digite o valor total: '))

valor_total_com_desconto = valor_total * 0.9
valor_de_cada_parcela = valor_total / 3
comissão_do_vendedor = valor_total_com_desconto * 0.05
comissão_do_vendedor_venda_parcelada = valor_total * 0.05

print(f'o total a pagar com desconto de 10%: {valor_total_com_desconto}')
print(f'o valor de cada parcela, no parcelamento de 3× sem juros: {valor_de_cada_parcela}')
print(f'a comissão do vendedor, no caso da venda ser a vista: {comissão_do_vendedor}')
print(f'a comissão do vendedor, no caso da venda ser parcelada: {comissão_do_vendedor_venda_parcelada}')
