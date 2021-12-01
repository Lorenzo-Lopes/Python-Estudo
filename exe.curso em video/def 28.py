import random

n = random.randrange(1, 5)
x = int(input('Digite o numero que o pc escolher entre 1 e 5: '))

print('voce digitou {} e o pc pensou em {}'.format(n, x))
if n == x:
    print('parabens voce acertou')
else:
    print('que burro da 0 pra ele')
