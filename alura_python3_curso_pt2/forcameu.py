def jogar():
    print("*-*" * 12)
    print("     Bem vindo ao jogo da Froca!")
    print("*-*" * 12)

    palavra_secreta ='banana'
    enforcou = False
    acertou = False


    while (not enforcou and not acertou):
        chute = input("Digite uma letra: ")

        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                print("Encontrei a letra '{}' na posição: {}".format(chute, index + 1))

            index+=1




        print('jogando')

    print("Fim do jogo")
if (__name__ == "__main__"):
        jogar()

