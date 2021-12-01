nome = str(input('Digite seu nome completo')).strip()

print(nome.lower())
print(nome.upper())
print(len(nome.replace(' ', '')))
print(len(nome)-nome.count(' '))
print(len(' '.join(nome.split())))
print(len(nome.split()[0]))

