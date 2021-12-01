import random
import time

print('-=+=-' * 6)
print('    \033[1;31;40m VAMOS JOGAR JOKENPO? \033[m')
print('-=+=-' * 6)
print('Suas opcoes são ')
print('''1 - PEDRA
2 - PAPEl
3 - TESOURA''')
op = int(input('Faça sua escolha:'))
opc = random.randint(1, 3)
print('Analisando', end='')
time.sleep(0.2)
print('.', end='')
time.sleep(0.2)
print('.', end='')
time.sleep(0.2)
print('.')
print('Voce escolheu {}'.format(opc))
if opc == 1:
    print('a maquina escolheu PEDRA')
elif opc == 2:
    print('a maquina escolheu PAPEL')
else:
    print('a maquina escolheu TESOURA ')

'''if op == opc:
    print('EMPATE!')
elif op == 1 and opc == 2 :
    print('DERROTA')
elif op == 1 and opc == 3:
    print('VITORIA')
elif op == 2 and opc == 1:
    print('VITORIA')
elif op == 2 and opc == 3:
    print('DERROTA')
elif op == 3 and opc == 1:
    print('DERROTA')
elif op == 3 and opc == 2:
    print('VITORIA')'''
if op == opc:
    print('EMPATE!')
elif op == 1 and opc == 3 or op == 3 and opc == 2 or op == 2 and opc == 1:
    print('VITORIA')
elif op == 2 and opc == 3 or op == 1 and opc == 2 or op == 3 and opc == 1:
    print('DERROTA')

