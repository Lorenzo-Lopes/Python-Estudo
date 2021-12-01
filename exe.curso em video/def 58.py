import random
cont = 0
rand = random.randint(1, 10)
opc = 0
print('\033[34;42;1mVamos Brincar De Adivinhação?\033[m')
while rand != opc:
    opc = int(input('Tente adivinhar o numero que eu estou pensando.[1/10] >'))
    if opc > 10 or opc < 1:
        print('Numero invalido,tente novamente.')
    elif opc != rand:
        if opc > rand:
            print('Menos...', end='')
        else:
            print('Mais...', end='')
        print('Voce errou, tente novamente ')
    cont += 1
print('Voce escolheu {}'.format(opc))
print('A Maquina escolheu {}'.format(rand))
if cont == 1:
    print('VOCE É INCRIVEL, ACERTOU DE PRIMEIRA.')
else:
    print('Parabens, Voce acertou na {}ª tentativa'.format(cont))
