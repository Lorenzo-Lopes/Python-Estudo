def multiplica(*args):
    resultado = 1
    for i in args:
        resultado = resultado*i
    return resultado
numero = 1,2,3,4,5,6,7,8,9,10
#numero = 3,5

def par_impar(n):
    return 'PAR' if n%2==0 else 'IMPAR'
    

n_multiplicados = multiplica(*numero)
par_impar = par_impar(n_multiplicados)

print(f"O resultado da multiplicação é: {n_multiplicados}")
print(par_impar)
