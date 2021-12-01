n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))

menor = n1
maior =n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

if n2 < n1 and n2 <n3:
    menor =n2
if n3 < n1 and n3 < n2:
    menor = n3

print('{} é o maior numero e o {} é o menor numero'.format(maior, menor))