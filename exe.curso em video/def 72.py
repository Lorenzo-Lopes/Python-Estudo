tup = ('um', 'dois', 'tres', 'quatro', 'cinco','seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito ', 'dezenove', 'vinte')
num = int(input('Digite um numero'))
while num <1 or num >20:
    num = int(input('Valor Invalido. Tente novamente'))
print(f'O numero digitado foi {tup[num-1]}')
