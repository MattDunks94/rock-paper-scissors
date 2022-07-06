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
            print("\nIt's a draw!")
        elif player == "rock":
            if opposition == "paper":
                print("\nYou lose!", opposition, "covers", player)
            else:
                print("\nYou win!", player, "crushes", opposition)
        elif player == "paper":
            if opposition == "scissors":
                print("\nYou lose!", opposition, "slices", player)
            else:
                print("You win!", player, "covers", opposition)
        elif player == "scissors":
            if opposition == "rock":
                print("You lose!", opposition, "crushes", player)
            else:
                print("\nYou win!", player, "slices", opposition)
        else:
            print("\nWe do not have that in our inventory!")
            print("Please choose 1 of the 3 options available.")
        
                
print("\n---------------------")
print("ROCK, PAPER, SCISSORS")
print("---------------------")

game_start()