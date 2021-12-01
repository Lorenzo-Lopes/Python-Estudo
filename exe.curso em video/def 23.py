'''import math
n = str(input('Digite um numero entre 0 e 9999'))
n2 = ' '.join(n)
n3 = n2.split()
print(n2)
print('a unidade é {}'.format(n3[3]))
print('a dezena é {}'.format(n3[2]))
print('a centena é {}'.format(n3[1]))
print('o milhar é {}'.format(n3[0]))'''

num = int(input('digite um numero'))
un = num % 10
de = num//10 % 10
ce = num // 100 %10
mi = num // 1000 %10
print('unidade {}\n dezena {} \n centena {} \n milhar {}'.format(un,de,ce,mi))

