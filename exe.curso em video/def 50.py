soma=0
for c in range(1, 7):
    dig = int(input('Digite um valor '))
    if dig % 2 == 0:
        soma += dig
print(soma)
