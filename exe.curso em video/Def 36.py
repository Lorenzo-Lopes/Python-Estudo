import time
casa = float(input('Digite o valor da casa que voce deseja comprar: \033[0;32;0 mR$\033[m'))
par = int(input('Em quantos anos vai pagar? '))
vpar = casa / (par*12)
print('A casa no valor de {} vai custar {:.2f} se voce pagar em  {} anos'.format(casa, vpar, par))
sal = float(input('Digite seu salario '))
print('-=-'*10)
print('ANALISANDO...')
print('-=-'*10)
time.sleep(2)
if vpar <= (sal*30/100):
    print('\033[1;30;42mCondição aprovada\033[m')
else:
    print('\033[1;30;41mReprovado\033[m')

