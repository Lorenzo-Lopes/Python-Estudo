"""calculadora utilizando while, con verificações de input."""

continuar = False
operadores_validos = '+-*/'

while continuar is not True:
    try:
        num1 = float(input("Digite um numero: "))
        num2 = float(input("Digite um numero: "))
        numero_validos = True
    except:
        print("O numero digitado é invalido.")
        numero_validos=None
        continue
    
    op = input(" Digite um Operador (+-*/)")

    if op not in operadores_validos:
        print("Operador selecionado invalido, tente novamente.")
        continue

    if len(op) > 1 :
        print("Digite apenas um operador.")
        continue

    op = operadores_validos.index(op)
    if op ==0:
        print(num1+num2)
    if op ==1:
        print(num1-num2)
    if op ==2:
        print(num1*num2)
    if op ==3:
        print(num1/num2)

    continuar = input("Digite [s]air  para interromper a execução da calculadora").lower().startswith('s')
    if continuar == '':
        continuar=False
