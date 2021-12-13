def jogar():
    print("*-*" * 12)
    print("     Bem vindo ao jogo da Froca!")
    print("*-*" * 12)

    palavra_secreta ='banana'.upper()
    letras_acertadas = ['_' for lentra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while (not enforcou and not acertou):

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    print("Encontrei a letra '{}' na posição: {}".format(chute.lower(), index + 1))
                    letras_acertadas[index] = letra
                index +=  1
        else:
            erros += 1
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
    if (acertou):
        print('Voce ganhou')
    else:
        print('Voce perdeu')
    print("Fim do jogo")
if (__name__ == "__main__"):
        jogar()

