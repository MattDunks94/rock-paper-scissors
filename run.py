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
    check every possible combination of game results.
    """
    player = False
    while player == False:
        player = input("Rock, Paper, Scissors?")
        if player == opposition:
            print("It's a draw!")
        elif player == "rock":
            if opposition == "paper":
                print("You lose!", opposition, "covers", player,".")

print("\n---------------------")
print("ROCK, PAPER, SCISSORS")
print("---------------------")

game_start()
