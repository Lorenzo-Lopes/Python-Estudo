import random
tup = (random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10))
print(tup)
print('O menor numero sorteado foi:{}'.format(sorted(tup)[0]))
print(f'O maior numero sorteado foi:{sorted(tup)[-1]}')
