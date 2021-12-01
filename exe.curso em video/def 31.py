km = int(input('Quanto voce vai rodar?'))
if km <= 200:
    pas = km * 0.5
    print('a passagem vai custa R${}'.format(pas))
else:
    pas = km * 0.45
    print('a passagem vai custaR#{}'.format(pas))