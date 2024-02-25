import random

def jogar_forca():
    print("Bem-vindo ao jogo da forca!")
    palavras = ["casa", "carro", "python", "programacao", "jogo", "forca"]
    palavra_secreta = random.choice(palavras)
    letras_acertadas = ["_" for _ in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    desenhos = ['''
    +---+
    |   |
        |
        |
        |
        |
    =======''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =======''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =======''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =======''', '''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =======''', '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =======''', '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =======''']

    print("Palavra: ", " ".join(letras_acertadas))

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(desenhos[erros])
            print("Você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print("Palavra: ", " ".join(letras_acertadas))

    if(acertou):
        print("Parabéns, você ganhou!")
    else:
        print("Você perdeu! A palavra era {}".format(palavra_secreta))

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar_forca()
