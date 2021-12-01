p = float(input('Digite seu peso: '))
a = float(input('Digite sua altuta: '))

imc =p / (a**2)
print('Seu IMC é {:.2f}'.format(imc))
if imc< 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('sobre peso')
elif imc < 40:
    print('Obesidade')
else:
    print('obesidade morbida')