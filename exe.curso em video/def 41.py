from datetime import date
import time
idade = int(input('Digite sua idade'))
atual = date.today().year
idade =  atual - idade
print(atual)
print('Sua categoria é...')
time.sleep(2)
if idade < 9:
    print('MIRIM')
elif idade < 14:
    print('infantil')
elif idade < 19:
    print('Junior')
elif idade < 25:
    print('senior')
elif idade >= 25:
    print('master')
