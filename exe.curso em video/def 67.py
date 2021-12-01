tab = cont = 0
while True:
    num = int(input('Qual tabuada voce quer ver?'))
    if num < 0:
        break
    else:
        for c in range(1, 11):
            print(f'{num} X {c} = {num*c}')

