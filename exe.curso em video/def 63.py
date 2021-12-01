n = int(input('Digite quantos numero voce quer ver da Sequencia de Fibonacci'))
#print('Os {} primeiros numeros da sequencia de fibo são:'.format(n), end=' ')
cont = 0
sq1 = 0
sq2 = 1
soma = 1
while cont != n:
    print(sq1, end='-')
    soma = sq2 + sq1
    sq1 = sq2
    sq2 = soma
    cont += 1

