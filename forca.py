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