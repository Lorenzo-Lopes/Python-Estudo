def jogar():
    print("*-*" * 12)
    print("     Bem vindo ao jogo da Froca!")
    print("*-*" * 12)

    palavra_secreta ='banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    enforcou = False
    acertou = False


    while (not enforcou and not acertou):
        print(letras_acertadas)
        chute = input("Digite uma letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra '{}' na posição: {}".format(chute.lower(), index + 1))
                letras_acertadas[index] = chute
            index += 1




        print('jogando')

    print("Fim do jogo")
if (__name__ == "__main__"):
        jogar()

