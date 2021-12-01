t1 = float(input('digite um lado'))
t2 = float(input('digite o segundo lado'))
t3 = float(input('Digite o terceiro lado'))
if t1 < t2+t3 and t2 < t1+t3 and t3 < t1+t2:
    print('Forma um triangulo')
    if t1 == t2 == t3:
        print('Forma um triangulo equilatero')
    elif t1 == t2 or t1 == t3 or t2 == t3:
        print('Forma um triangulo isoceles')
    elif t1 != t2 != t3 != t1:
        print('forma um triangulo escaleno')

else:
    print('NAO Forma um triangulo')
