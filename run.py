# Import randint to create random integers.
from random import randint

# Create player options list.
player_options = ["rock", "paper", "scissors"]

# Assign the opposition to a random list item.
opposition = player_options[randint(0, 2)]

def game_start():
    """
    Assign the player to False, allowing them to choose their 
    option. Create a while loop and use if/else statements to 
    check every possible combination of game outcomes.
    """
    player = False
    while player == False:
        player = input("Rock, Paper, Scissors? ")
        if player == opposition:
            print("\nIt's a draw!\n")
        elif player == "rock":
            if opposition == "paper":
                print("\nYou lose!", opposition, "covers", player, "\n")
            else:
                print("\nYou win!", player, "crushes", opposition, "\n")
        elif player == "paper":
            if opposition == "scissors":
                print("\nYou lose!", opposition, "slices", player, "\n")
            else:
                print("\nYou win!", player, "covers", opposition, "\n")
        elif player == "scissors":
            if opposition == "rock":
                print("You lose!", opposition, "crushes", player, "\n")
            else:
                print("\nYou win!", player, "slices", opposition, "\n")
        else:
            print("\nWe do not have that in our inventory!")
            print("Please choose 1 of the 3 options available.\n")


        
                
print("\n---------------------")
print("ROCK, PAPER, SCISSORS")
print("---------------------")

game_start()