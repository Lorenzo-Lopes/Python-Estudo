import random
n1 = str(input('nome 1='))
n2 = str(input('nome 2='))
n3 = str(input('nome 3='))
n4 = str(input('nome 4='))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('nova ordem{}'.format(lista))
