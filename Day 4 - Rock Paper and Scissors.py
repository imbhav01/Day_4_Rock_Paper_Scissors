import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?").lower()
    if player == computer:
        print("computer : ", computer)
        print("player : ", player)
        print("Tie!")
    elif player == "rock":
        if computer == "scissors":
            print("computer : ", computer)
            print("player : ", player)
            print("player wins !")
        if computer == "paper":
            print("computer : ", computer)
            print("player : ", player)
            print("computer wins !")

    elif player == "paper":
        if computer == "scissors":
            print("computer : ", computer)
            print("player : ", player)
            print("computer wins !")
        if computer == "rock":
            print("computer : ", computer)
            print("player : ", player)
            print("player wins !")

    elif player == "scissors":
        if computer == "rock":
            print("computer : ", computer)
            print("player : ", player)
            print("computer wins !")
        if computer == "paper":
            print("computer : ", computer)
            print("player : ", player)
            print("player wins !")

    play_again = input("Play again? (Yes/No): ").lower()

    if play_again != "yes":
        break
print(" Bye ! ")