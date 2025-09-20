"""Gerando CPF"""
from random import randint
nove_inicio=''
for i in range(9):
    nove_inicio += str(randint(1,9))


contador= 10
soma_primeiro_digito= 0
for num in nove_inicio:
    soma_primeiro_digito += int(num)*contador
    contador-=1
soma_primeiro_digito = (soma_primeiro_digito*10)
prim_digito= soma_primeiro_digito%11 if soma_primeiro_digito%11 <= 9  else 0
prim_digito=soma_primeiro_digito%11

dez_inicio= nove_inicio+str(prim_digito)

contador= 11
soma_segundo_digito= 0
for num in dez_inicio:
    soma_segundo_digito += int(num)*contador
    contador-=1
soma_segundo_digito = (soma_segundo_digito*10)
seg_digito= soma_segundo_digito%11 if soma_segundo_digito%11 <= 9  else 0


cpf_verificado = dez_inicio+str(seg_digito)

print(cpf_verificado)