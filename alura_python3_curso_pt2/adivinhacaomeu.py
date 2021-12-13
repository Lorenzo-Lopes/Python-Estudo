import random


def jogar():
    print("*-*" * 12)
    print("  Bem vindo ao jogo de Adivinhação!")
    print("*-*" * 12)
    print("  1-Facil --- 2-Medio --- 3-Dificil")
    escolha = int(input("Escolha a dificuldade: "))
    pontuacao = 1000
    while (escolha < 0) or (escolha > 3):
        escolha = int(input("Escolha a dificuldade entre 1 e 3: "))

    if escolha == 1:
        print("facil")
        secreto = random.randrange(1, 101)
        total_de_tentativas = 10
        n = 101
    elif escolha == 2:
        secreto = random.randrange(1, 151)
        total_de_tentativas = 5
        n = 151
    elif escolha == 3:
        secreto = random.randrange(1, 201)
        total_de_tentativas = 2
        n = 201

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e {}: ".format(n - 1)))
        print("Você digitou ", chute)

        if chute < 1 or chute > n:
            print("Você deve digitar um número entre 1 e {}!".format(n - 1))
            print('*-*' * 12)
            continue

        acertou = chute == secreto
        maior = chute > secreto
        menor = chute < secreto

        if acertou:
            print("Você acertou!")
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior do que o número secreto.")
                # x = abs(chute - secreto)
                pontuacao -= abs(chute - secreto)
            elif menor:
                print("Você errou! O seu chute foi menor do que o número secreto.")
                pontuacao -= abs(chute - secreto)

    print('O valor correto era: {}'.format(secreto))
    print('Sua pontuação final foi de: {}'.format(pontuacao))
    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
