print('-+=+'*8 +'\n  PROGRAMA DE ANALISE DE MEDIA\n'+'-+=+'*8)
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
med = (n1+n2)/2
print('SUA MEDIA FOI {}.'.format(med))

if med >= 7:
    print('\033[1;30;42mAPROVADO\033[m')
elif med >= 5 and med <=6.9:
    print('RECUPERAÇÃO')
elif med < 5:
    print('\033[1;30;41mREPROVADO\033[m')