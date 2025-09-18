print("Adivinhação de palavra secreta")

palavra_secreta = "Palavra"
palavra_secreta_min = palavra_secreta.lower()
tamanho_palavra_secreta = "*"*len(palavra_secreta)
letras_acertadas=''
palavra_formatada= ''
tentativas=0

while True:
    palavra_formatada=''
    palpite = input("Digite uma letra")
    if len(palpite) > 1:
        print("Digite apenas uma letra.")
        continue
    if palpite in palavra_secreta_min:
        letras_acertadas += palpite
    for letra in palavra_secreta_min:
        if letra in letras_acertadas:
            palavra_formatada+=letra
        else :
            palavra_formatada+='*'
    if palavra_formatada == palavra_secreta_min:
        break
    tentativas+=1
    print(palavra_formatada)
       
print(f"Voce levou {tentativas}x para acertar a palavra: {palavra_secreta}")

