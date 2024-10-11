"""
the computer will choose a random number 1 to 100
the user will guess numbers, getting told too high or low, until they get the right answer
"""

import random

minimum = 1
maximum = 100

computer_num = random.randint(minimum, maximum)
player_guess = 0 
counter = 0

while player_guess != computer_num:
    player_guess = int(input("Guess a number: "))
    if player_guess > computer_num:
        print("Too High")
    elif player_guess < computer_num:
        print("Too Low")
    else:
        pass
    counter += 1

print("Correct! It took you ", counter, " guesses")

