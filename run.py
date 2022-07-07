# Import randint to create random integers.
from random import randint

# Create player options list.
player_options = ["rock", "paper", "scissors"]

# Assign the opposition to a random list item.
cpu = player_options[randint(0, 2)]

def game_start():
    """
    Assign the player to False, allowing them to choose their 
    option. Create a while loop and use if/else statements to 
    check every possible combination of game outcomes.
    """
    player_score = 0
    cpu_score = 0
    player = False

    while player == False:
        player = input("Rock, Paper, Scissors? ")
        if player == cpu:
            print("\nIt's a draw!\n")
        elif player == "rock":
            if cpu == "paper":
                print("\nYou lose!", cpu, "covers", player, "\n")
                cpu_score += 1
            else:
                print("\nYou win!", player, "crushes", cpu, "\n")
                player_score += 1
        elif player == "paper":
            if cpu == "scissors":
                print("\nYou lose!", cpu, "slices", player, "\n")
                cpu_score += 1
            else:
                print("\nYou win!", player, "covers", cpu, "\n")
                player_score += 1
        elif player == "scissors":
            if cpu == "rock":
                print("You lose!", cpu, "crushes", player, "\n")
                cpu_score += 1
            else:
                print("\nYou win!", player, "slices", cpu, "\n")
                player_score += 1
        else:
            print("\nWe do not have that in our inventory!")
            print("Please choose 1 of the 3 options available.\n")


    
    print("Your Score:", player_score)
    print("CPU Score:", cpu_score)

                
print("\n---------------------")
print("ROCK, PAPER, SCISSORS")
print("---------------------")

game_start()