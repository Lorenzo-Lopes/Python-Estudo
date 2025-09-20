"""Calculando CPF"""

#cpf =input("Informe seu CPF: ")
#cpf = "962.543.580-85"
cpf = "316.993.768.59"
#cpf = "145.382.206-20"
#cpf = "746.824.890.70"
cpflimpo = cpf.replace(".","")
cpflimpo = cpflimpo.replace("-","")
digitos = cpflimpo[9::]
nove_inicio= cpflimpo[0:9:]
print(nove_inicio)

contador= 10
soma_primeiro_digito= 0
for num in nove_inicio:
    print(num, contador, int(num)*contador)
    soma_primeiro_digito += int(num)*contador
    contador-=1
soma_primeiro_digito = (soma_primeiro_digito*10)
prim_digito= soma_primeiro_digito%11 if soma_primeiro_digito%11 <= 9  else 0
prim_digito=soma_primeiro_digito%11
print(soma_primeiro_digito)
print(prim_digito)
dez_inicio= nove_inicio+str(prim_digito)

contador= 11
soma_segundo_digito= 0
for num in dez_inicio:
    print(num, contador, int(num)*contador)
    soma_segundo_digito += int(num)*contador
    contador-=1
soma_segundo_digito = (soma_segundo_digito*10)
seg_digito= soma_segundo_digito%11 if soma_segundo_digito%11 <= 9  else 0
print(seg_digito)

cpf_verificado = dez_inicio+str(seg_digito)
if cpf_verificado == cpflimpo:
    print(f"Cpf: {cpf_verificado} VALIDO!")
else:
    print(f"Cpf: `{cpf_verificado} Invalido!")