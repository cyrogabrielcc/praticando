import random
def hangman():

    word = random.choice(["vasco" , "botafogo" , "flamengo" , "palmeiras" , "corinthians" , "santos" , "fluminense" , "america" , "bragantino" , "saopaulo", "vitoria", 'sport'  ])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("BOOOOOOA PATRÃO!!!")
            break

        print("Advinhe o Time:" , main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            guess = input("Ecreva um caracter válido: ")

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9")
                print("  --------  ")
            if turns == 8:
                print("8")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1")
                print("Tá quase morrendo, você ainda tem uma chance!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("PERDEEEEEEEEEEEEEEEEEEEEEEEEEEEEU KKKK")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\     ")
                print("    / \     ")
                break


name = input("Entre com seu nome: ")
print("Bem vindo" , name )
print("-------------------")
print("Tente advinhar o time de futebol em até 10 tentativas. Vamos lá! ") 
hangman()
print()