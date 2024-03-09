import random
from os import system, name

def limpar_tela():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')

def game():
    limpar_tela()

    print("\nBem-vindo(a) ao Hangman!")
    print("Adivinhe a Palavra abaixo: \n")

    palavras = ["banana", 'pera', 'maca', 'morango', 'laranja']
    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]

    chances = 6

    letras_erradas = []

    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\n Chances restantes:", chances)
        print("Letras erradas:", letras_erradas)

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:            
            for index, letra in enumerate(palavra):
                if tentativa == letra:
                    letras_descobertas[index] = letra
                    index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era: ", palavra)
            break
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era: ", palavra)

if __name__ == "__main__":
    game()
    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")