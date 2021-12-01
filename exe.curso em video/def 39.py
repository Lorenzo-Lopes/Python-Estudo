from datetime import date

nas = int(input('Digite sua idade:'))
ano = date.today().year
id = ano - nas
print('sua idade é {}'.format(id))
if id < 18:
    print('faltam {} anos para se alistar'.format(18-id))
elif id == 18:
    print('{}é o ano para se alistar'.format(ano))
elif id> 18:
    print('voce deveria ter se alistado a {} anos'.format((id-18)))