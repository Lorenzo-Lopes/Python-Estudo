'''
sexo =''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite se seu genero[M/F]')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Genero invalido. Tente novamente!')
if sexo == 'M':
    print('Voce é um Homem.')
else:
    print('Voce é uma Mulher'
'''
sexo = str(input('Informe seu Genero[M/F]')).strip().upper()[0]
while sexo !='M' and sexo !='F':
    sexo = str(input('Valor informado invalido. \nPorfavor tente novamente:')).strip().upper()[0]
print('O genero digitado é {}'.format(sexo))
