'''import random
x = ('a', 'b', 'c', 'd')
print('valor sorteado ={}'.format(x[random.randint(0, 3)]))'''

from random import choice
n1 = str(input('nome 1='))
n2 = str(input('nome 2='))
n3 = str(input('nome 3='))
n4 = str(input('nome 4='))
lista = [n1, n2, n3, n4]
print('o nome escolhido foi {}'.format(choice(lista)))
