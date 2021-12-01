import os
menu = 0
res = 0
n1 = float(input('Digite um numero. '))
n2 = float(input('Digite outro numero'))
print("-=-" * 10)
print('''    [1] - SOMAR
    [2] - MULTIPLICAR
    [3] - MAIOR NUMERO
    [4] - NOVOS NUMEROS
    [5] - SAIR DO PROGRAMA''')
print("-=-" * 10)

while menu != 5:
    menu = int(input('Oque voce quer fazer com esses numeros?'))
    if menu == 1:
        res = n1+n2
        print('Soma entre {} e {} é igual  a:{}'.format(n1,n2,res))
    elif menu == 2:
        res = n1 * n2
        print('A Multiplicação entre {} e {} é igual  a:{}'.format(n1, n2, res))
    elif menu == 3:
        if n1 == n2:
            print('Eles são iguais')
        elif n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
        else:
            print(f'{n2} é maior que {n1}.')
    elif menu == 4:
        n1 = float(input('Digite um numero. '))
        n2 = float(input('Digite outro numero'))
        print("-=-" * 10)
        print('''    [1] - SOMAR
    [2] - MULTIPLICAR
    [3] - MAIOR NUMERO
    [4] - NOVOS NUMEROS
    [5] - SAIR DO PROGRAMA''')
        print("-=-" * 10)
    elif menu == 5:
        print('Finalizando...')
        sair = 5
    else:
        print('Opção invalida, Tente novamente')

