import random
import time
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('''Suas opções são...
0 - PEDRA
1 - PAPEL
2 - TESOURA''')
op = int(input('Escolha uma das opções '))

print('JO ', end='')
time.sleep(0.5)
print('KEN ', end='')
time.sleep(0.5)
print('PÔ! ')
time.sleep(0.5)
print('Voce escolheu >{}<'.format(itens[op]))
opc = random.randint(0, 2)
print('O computador escolheu >{}<'.format(itens[opc]))

if op == opc:
    print('EMPATE!')
elif op == 0 and opc == 2 or op == 2 and opc == 1 or op == 1 and opc == 0:
    print('VITORIA')
'''elif op == 1 and opc == 2 or op == 0 and opc == 1 or op == 2 and opc == 0:
    print('DERROTA')'''



