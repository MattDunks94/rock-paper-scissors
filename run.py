# Import randint to create random integers.
from random import randint

# Create player options list.
player_options = ["rock", "paper", "scissors"]

# Assign the opposition to a random list item.
opposition = player_options[randint(0, 2)]
