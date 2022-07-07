# Import randint to create random integers.
from random import randint

# Create player options list.
player_options = ["rock", "paper", "scissors"]


def start_game():
    """
    This function offers the user to play or not.
    If user types 'y' the main_game function is executed.
    If the user types 'n' the program will terminate.
    If the user enters anything other than 'y' or 'n' the 
    start_game function re-executes.
    """
    play = input("Start Game? Y / N ")

    if play == "y":
        main_game()
    elif play == "n":
        quit()
    else:
        print("\nNot a valid answer. Please try again.\n")
        start_game()


def main_game():
    """
    Assign the player to False, allowing them to choose their 
    option. Create a while loop and use if/else statements to 
    check every possible combination of game outcomes.
    """
    player_score = 0
    cpu_score = 0
    player = False

    # Assign the opposition to a random list item from player_options.
    cpu = player_options[randint(0, 2)]

    while player == False:

        player = input("\nRock, Paper, Scissors?\n")
        if player == cpu:
            print(player, "VS", cpu, "\n")
            print("It's a DRAW!\n")
        elif player == "rock":
            if cpu == "paper":
                print(player, "VS", cpu, "\n")
                print("You LOSE!", cpu, "covers", player, "\n")
                cpu_score += 1
            else:
                print(player, "VS", cpu, "\n")
                print("You WIN!", player, "crushes", cpu, "\n")
                player_score += 1
        elif player == "paper":
            if cpu == "scissors":
                print(player, "VS", cpu, "\n")
                print("You LOSE!", cpu, "slices", player, "\n")
                cpu_score += 1
            else:
                print(player, "VS", cpu, "\n")
                print("You WIN!", player, "covers", cpu, "\n")
                player_score += 1
        elif player == "scissors":
            if cpu == "rock":
                print(player, "VS", cpu, "\n")
                print("You LOSE!", cpu, "crushes", player, "\n")
                cpu_score += 1
            else:
                print(player, "VS", cpu, "\n")
                print("You WIN!", player, "slices", cpu, "\n")
                player_score += 1
        else:
            print("\nWe do not have that in our inventory!")
            print("Please choose 1 of the 3 options available.\n")
        player = False
        cpu = player_options[randint(0, 2)]

        print("Your Score:", player_score)
        print("CPU Score:", cpu_score)


def main():
    # All functions created into one main function.
    start_game()
    main_game()


print("\n---------------------")
print("ROCK, PAPER, SCISSORS")
print("---------------------")

main()