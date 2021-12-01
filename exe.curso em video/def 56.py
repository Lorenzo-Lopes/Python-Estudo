somaida = 0  # SOMA DE IDADE
medidade = 0  # MEDIA DE IDADE DO GRUPO
homemvelhon = ''  # NOME DO HOMEM MAIS VELHO
homemvelhoi = 0  # IDADE NO HOMEM MAIS VELHO
somam20 = 0  # MULHER COM MENOS DE 20 ANOS
for p in range(1, 5):  # PEGA A INFORMAÇÃO DE 4 PESSOAS
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('NOME:'))
    idade = int(input('IDADE:'))
    sex = str(input('SEXO [F/M])')).upper()
    somaida += idade
    if p == 1 and sex == 'M':  # VERIFICA SE É O HOMEM MAIS VELHO
        homemvelhoi = idade
        homemvelhon = nome
    if sex == 'M' and idade > homemvelhoi:  # VERIFICA A IDADE DO HOMEM MAIS VELHO
        homemvelhoi = idade
        homemvelhon = nome
    if sex == 'F' and idade < 20:   #SOMA A IDADE DAS MULHERES
        somam20 += 1
medidade = somaida / 4 #FAZ A SOMA DA MEDIA DE IDADE
print('A IDADE MEDIA DO GRUPO É {} ANOS.'.format(medidade)) #MOSTRA MEDIA DE IDADE
print('O homem mais velho é o {} e tem {} anos. '.format(homemvelhon, homemvelhoi)) #NOME E IDADE DO HOMEM MAIS VELHO
if somam20 > 0: #VERIFICA SE TEM MULHERES MENOR DE 20 ANOS
    print('No grupo tem {} mulheres com menos de 20 anos.'.format(somam20))#PRINTA QUANTAS MULHERES TEM MENOS DE 20 ANOS
else:
    print('Nenhuma mulher do grupo tem menos de 20 anos.')#PRINTA CASO NAO TENHA MULHERES MENORES DE 20 ANOS
