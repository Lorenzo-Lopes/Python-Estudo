soma = soma1000 = menor = cont = 0
nomemenor = ' '
while True:
    sair = ' '
    nome = str(input('Nome:'))
    prod = float(input('Valor R$:'))
    while sair not in 'SsNn':
        sair = str(input('Deseja comprar outro produto?[S/N]')).upper().strip()[0]
    cont += 1
    if prod >= 1000:
        soma1000 += 1
    if cont == 1 or prod < menor:
        menor = prod
        nomemenor = nome
    soma += prod
    if sair == 'N':
        break
print(f'A soma dos final dos produtos foi de R$.{soma}')
print(f'no final {soma1000} custaram mais que R$.1000,00 ')
print(f'Custando {menor} o produto mais barato foi a/o {nomemenor}')