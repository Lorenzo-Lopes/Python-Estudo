pt = int(input('Digite o primeiro termo de um PA:'))
rz = int(input('Digite a razão da PA:'))
tr = int(input('Quantos termos voce quer ver ?'))
sair = -1
while sair != 0:

    while tr > 0:
        print(pt)
        pt = pt+rz
        tr -= 1
    if tr == 0:
        tr = int(input('Quantos termos voce quer ver ?'))
        if tr == 0:
            sair = 0
