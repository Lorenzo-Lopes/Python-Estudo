val = int(input('Digite o valor a ser convertido'))
print('-=-'*12)
print(' Ditete 1 para BINARIO \n Digite 2 para OCTAL \n Digite 3 para HEXADECIAMAL')
print('-=-'*12)
op = int(input('Escolha uma das opções acima:'))
print('-=-'*12)

if op == 1:
    print ('{} em binario é {} '.format(val, bin(val)[2:]))
elif op == 2:
    print('{} em octal é {}'.format(val, oct(val)[2:]))
else:
    print('{} em hexadeciamal é {}'.format(val, hex(val)[2:]))