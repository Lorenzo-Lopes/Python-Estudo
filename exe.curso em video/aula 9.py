frase = 'Curso em Video Python'
print('{}'.format(frase[9::3]))#motras da posição 9 até o fnal pulando de 3 em 3
print(len(frase))#mostra a quantidade de caracteras na string
print(frase.count('o', 0, 13))#conta quando 'o' tem entra a posição 0 e 12 -- 13 nao é inclusa
print(frase.find('deo'))#mostra o inicio da string
print(frase.find('Android'))#caso nao encontre retorna -1
print('Cursor'in frase)#retorna T/F se tem 'Curso' dentro da var frase
print("""teste
print
em
linhas
dividas""")

'''Transformação de string'''
print(frase.replace('Python', 'Android')) # troca os caracteres da primeira posição pelos da segunda
print(frase.upper())#MAIUSCULO
print(frase.lower())#minusculo
print(frase.capitalize()) #deixa tudos minusculos exeto a primeira letra
print(frase.title())# todas as palavras com a primeira letra maiuscula
frase2 = '   Aprenda Python  '
print(frase2.strip()) #removes os ESPAÇOS do começo e fim da string
print(frase2.rstrip())#remove espaços a direita
print(frase2.lstrip())#remove espaços a esqueda
'''divisao'''
print(frase.split())# cada palavra vira um string--gera uma lista da string mae
'''junção'''
print('-'.join(frase))


