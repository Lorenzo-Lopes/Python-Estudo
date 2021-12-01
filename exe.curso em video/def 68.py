import random
cont = 1
pi = 'a'
print('Vamos jogar par ou impar?')
while True:
    num = int(input('Digite um numero'))
    rand = random.randint(1, 5)
    while pi not in '´PIpi':
        pi = str(input('Par ou Impar?[P/I]')).strip().upper()[0]
    if (num+rand) % 2 == 0 and pi == 'P':
        print(f'A soma dos numeros foi {num+rand}, portando voce Ganhou')
        cont += 1
    else:
        print(f'A soma dos numeros foi {num+rand}, portanto voce Perdeu')
        print(f'Voce perdeu na rodada {cont}')
        break



