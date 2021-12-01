print('Digite uma sequequencia  de numero que deseja sumar \n Digite 999 para encessar a sequencia')
soma = 0
dig = 0
cont = 0
while dig != 999:
    dig = int(input('>'))
    if dig != 999:
        soma= dig +soma
        cont +=1
print('No total foram somados:{} numeros, e a soma final foi de:{}'.format(cont, soma))