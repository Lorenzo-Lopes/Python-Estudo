num = int(input('Digite um numero'))
res = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        res += 1
    else:
        print('\033[031m', end=' ')
    print('{}'.format(c), end=' ')
if res == 2:
    print('\n{} é um numero primo'.format(num))
elif num == 1:
    print('\n1 Nao é um numero primo')
else:
    print('\n{} nao é um numero primo'.format(num))
