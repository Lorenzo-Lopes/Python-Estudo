frase = str(input('Digite um frase: ')).strip().replace(' ', '')
frase = list(frase)

#for c in range(1,len(frase)):
frase2 = frase[::-1]
    #print(frase2)
if frase== frase2:
    print('a frase é um palindromo')
else:
    print('a frase nao é um palindromo')