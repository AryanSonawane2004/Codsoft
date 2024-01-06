import random 

print("Welcome To Rock Paper Scissors Game")

cpuScore = 0
playerScore = 0
TieScore = 0
possibleOptions = ["Rock", "Paper", "Scissors"]

def checkforwinner(playerhand, computerhand):
    if(playerhand == "Rock" and computerhand == "Paper"):
        print("Game Over !! \n You Lose!!")
        return "CPU"
    elif(playerhand == "Rock" and computerhand == "Scissors"):
        print("Game Over !! \n You Win!!")
        return "PLAYER"
    elif(playerhand == "Paper" and computerhand == "Scissors"):
        print("Game Over !! \n You Lose!!")
        return "CPU"
    elif(playerhand == "Paper" and computerhand == "Rock"):
        print("Game Over !! \n You Win!!")
        return "PLAYER"
    elif(playerhand == "Scissors" and computerhand == "Rock"):
        print("Game Over !! \n You Lose!!")
        return "CPU"
    elif(playerhand == "Scissors" and computerhand == "Paper"):
        print("Game Over !! \n You Win!!")
        return "PLAYER"
    elif(playerhand == computerhand):
        print("It's a Tie, play again!!")
        return "TIE"
    else:
        return "Invalid Input"

while(playerScore != 3 and cpuScore != 3):
    while True:
        print("\n")
        playerhand = input("Player Hand:")
        
        if(playerhand == "Rock" or playerhand == "Paper" or playerhand == "Scissors"):
            break
        else:
            print("Invalid Input!!")
            break

    computerhand = random.choice(possibleOptions)

    print("Your Hand: ", playerhand)
    print("CPU Hand: ", computerhand)
    result = checkforwinner(playerhand, computerhand)
    if(result == "PLAYER"):
        playerScore += 1
    elif(result == "CPU"):
        cpuScore += 1
    elif(result == "TIE"):
        TieScore += 1
    else:
        break        

    print("PlayerScore: ", playerScore, "CPUScore: ", cpuScore, "TieScore: ", TieScore)

print("Thanks for playing!!!!")