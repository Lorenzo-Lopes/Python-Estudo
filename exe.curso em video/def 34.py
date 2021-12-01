sal = float(input('Digite seu salario'))
if sal >= 1250:
    sal = (sal * 10 / 100) + sal
else:
    sal = (sal * 15 / 100) + sal

print('seu novo salario é R${}'.format(sal))
