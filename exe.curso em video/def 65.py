print('Digite uma sequequencia  de numero que deseja sumar ')
soma = 0
sair = str('0')
dig = 0
cont = 0
while sair != 'n':
    dig = int(input('>'))
    sair = str(input('Quer continuar?'))
    soma = dig + soma
    cont += 1
print('No total foram somados:{} numeros, e a soma final foi de:{}'.format(cont, soma))