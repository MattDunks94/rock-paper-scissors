# Import randint to create random integers.
from random import randint

# Create player options list.
player_options = ["rock", "paper", "scissors"]

# Assign the opposition to a random list item from player_options.
cpu = player_options[randint(0, 2)]


def start_game():
    """
    This function offers the user to play or not.
    If user types 'y' the main_game function is executed.
    If the user types 'n' the program will terminate.
    If the user enters anything other than 'y' or 'n' the
    start_game function re-executes along with a message.
    """
    play = input("Start Game? Y / N\n").lower()

    if play == "y":
        main_game(cpu)
    elif play == "n":
        quit()
    else:
        print(f"\n{play} is not a valid response. Please try again.\n")
        start_game()


def main_game(cpu):
    """
    A while loop and if/else statements to check every possible
    combination of game outcomes. Also updates score for both the user
    and cpu. An if statement at the end of the loop checks whether player
    or cpu has scored 5. If so the start_game function executes, allowing
    the user to end or restart game.
    """

    # Assign player to False.
    player = False
    # Input to allow player to enter their name.
    player_name = input("Please enter player name:\n")
    print(player_name)

    # Player and cpu scores.
    player_score = 0
    cpu_score = 0

    while player is False:

        player = input("\nRock, Paper, Scissors?\n").lower()
        if player == cpu:
            print(f"{player} VS {cpu} \n")
            print("It's a DRAW!\n")
        elif player == "rock":
            if cpu == "paper":
                print(f"{player} VS {cpu} \n")
                print(f"{player_name} LOSES! {cpu} covers {player}.\n")
                cpu_score += 1
            else:
                print(f"{player} VS {cpu} \n")
                print(f"{player_name} WINS! {player} crushes {cpu}.\n")
                player_score += 1
        elif player == "paper":
            if cpu == "scissors":
                print(f"{player} VS {cpu} \n")
                print(f"{player_name} LOSES! {cpu} slices {player}.\n")
                cpu_score += 1
            else:
                print(f"{player} VS {cpu} \n")
                print(f"{player_name} WINS! {player} covers {cpu}.\n")
                player_score += 1
        elif player == "scissors":
            if cpu == "rock":
                print(f"{player} VS {cpu} \n")
                print(f"{player_name} LOSES! {cpu} crushes {player}.\n")
                cpu_score += 1
            else:
                print(f"{player} VS {cpu} \n")
                print(f"{player_name} WINS! {player} slices {cpu}.\n")
                player_score += 1
        else:
            print("\nWe do not have that in our inventory!")
            print("Please choose 1 of the 3 options available.\n")
        # Re-assign player and cpu values to restart the while loop.
        player = False
        cpu = player_options[randint(0, 2)]
        # Display scores.
        print(f"{player_name}'s Score: {player_score}\nCPU Score: {cpu_score}")

        # If statement to check if either player scores 5.
        if player_score == 5:
            print(f"{player_name} WINS!")
            start_game()
        elif cpu_score == 5:
            print(f"{player_name} LOST!")
            start_game()


def main():
    """
    All functions into one main function.
    """
    start_game()
    main_game(cpu)


# Introduces user to program and how to operate it.
print("-" * 21)
print("ROCK, PAPER, SCISSORS")
print("-" * 21, "\n")
print("Welcome to Rock, Paper, Scissors!")
print("Type your choice of weapon and hit enter.\nFirst to 5 wins!")

main()
