import forcameu
import adivinhacaomeu

def escolhe_jogo():
    print('/*/*/'*10)
    print('           Escolha o jogo que vai jogar.')
    print("/*/*/"*10)

    jogo = int(input('1- jogo de Adivinhação ou 2- jogo da Forca'))

    if (jogo == 1):
        print('Jogando forca')
        forcameu.jogar()

    elif(jogo == 2):
        print('Jogando Adivinhação')
        adivinhacaomeu.jogar()


if(__name__=="__main__"):
    escolhe_jogo()



