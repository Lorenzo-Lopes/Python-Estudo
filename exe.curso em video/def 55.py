p1 = 0
p2 = 0
for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if c == 1:
        p1 = peso
        p2 = peso
    else:
        if peso > p1:
            p1 = peso
        if peso < p2:
            p2 = peso

print('o menor peso foi {}'.format(p2))
print('o maior peso foi {}'.format(p1))
