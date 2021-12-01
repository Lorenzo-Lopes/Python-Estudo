mais18 = mmenos20 = homens = 0
while True:
    idade = int(input('Digite a idade'))
    sexo = str(input('Digite o genero [F/M]')).strip().upper()[0]
    while sexo not in 'mMfF':
        sexo = str(input('Digite o genero [F/M]')).strip().upper()[0]
    cas = str(input('Deseja cadastrar mais uma pessoa ?[S/N]')).strip().upper()
    while cas not in 'sSnN':
        cas = str(input('Deseja cadastrar mais uma pessoa ?[S/N]')).strip().upper()
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mmenos20 += 1
    if idade >= 18:
        mais18 += 1
    if cas == 'N':
        break
print(f'{mais18} pessoas tem mais de 18 anos ou  mais')
print(f'{homens} homens foram cadastrados')
print(f'{mmenos20} mulheres tem menos de 20 anos')