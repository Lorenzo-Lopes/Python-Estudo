from datetime import date
mai = 0
mer = 0
ano = date.today().year

for c in range(0, 7):
    nas = int(input('Digite seu ano de nascimento: '))
    if ano - nas >= 21:
        mai += 1
    else:
        mer += 1
print('{} são maior de idade '.format(mai))
print('{} são menor de idade '.format(mer))
