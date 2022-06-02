import random
totalguesses = 5
gameOver = False



while not gameOver:

    generator = random.randint(1,10)
    gamecomplete = False 
    nooftries = 0



    while not gamecomplete:
        guess = None

        inputguess = False



        while not inputguess:
            inputnumber = input("Guess a number between 1 and 10: ")

            if inputnumber == "-1":
                print("The number that is to be guessed is", generator)
            elif inputnumber.isdigit():
                guess = int(inputnumber)
                nooftries += 1 
                inputnumber = True
            else:
                print("That is not a positive number")


            if guess < generator:
                print("Your guess is too low")
            elif guess > generator:
                print("Your guess is too high")
            elif guess == generator:
                print("You win, correct guess")
            


    if nooftries == totalguesses:
        print("Game over, you used up all your guesses")
        print("The correct number was", generator)
        gamecomplete = True

playagain = input("Play again?")
if playagain == "n":
    gameOver = True
elif playagain == "N":
    gameOver = True


print("Game Over")