soma =  cont = 0
while True:
    n = int(input('Digire um valor. (para sair digite 999)'))
    if n == 999:
        break;
    else:
        soma += n
        cont += 1
print(f'a soma dos {cont} numeros foi {soma}')