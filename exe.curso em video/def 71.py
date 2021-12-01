print('-=-'*10)
print('        Banco do Lolo')
print('-=-'*10)
valor = int(input('Digite o valor a ser sacado:'))
saque = valor
nota = 50
notas = 0
while True:
    if saque >= nota:
        saque -= nota
        notas += 1
    else:
        if notas > 0:
            print(f'Sacadas {notas} de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        notas = 0
        if saque == 0:
            break