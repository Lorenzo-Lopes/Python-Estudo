val = float(input('valor do produto R$'))
print('1 - a vista')
print('2 - a vista cartão')
print('3 - 2x no cartão')
print('4 - 3x no cartão')

opc = int(input('seleciona a forma de pagamento.'))
if opc == 1:
    valf = val - (val*10)/100
    print('o valor do desconto é {}'.format(val-valf))
elif opc == 2:
    valf = val - (val*5)/100
    print('o valor do desconto é {}'.format(val - valf))
elif opc == 3:
    valf = val
elif opc == 4:
    valf = val+(val*20)/100
    print('o valor das parcelas é : {}'.format(valf/3))
print('o valor final do produto é {}'.format(valf))