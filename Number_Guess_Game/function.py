""" 
    Name : AbdElrahman Ibrahim Zaki
    Email : abdelrahmanzaki.aez@gmail.com  
    Project : C - Number Guess Game  - function file
"""
import random
import math

def play(winning_trial, losing_trial, trials):

    x = random.randint(1, 100)
    print("\n\tYou've only 10 chances to guess the integer!\n")
    
    # Initializing the number of guesses.
    count = 0
    
    # for calculation of minimum number of
    # guesses depends upon range
    while count < 10:
        count += 1
        # taking guessing number as input
        guess = int(input("Guess a number:- "))
        # Condition testing
        if x == guess:
            print("Congratulations you did it in ",
                count, " try")
            winning_trial += 1
            # Once guessed, loop will break
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")
    
    # If Guessing is more than required guesses,
    # shows this output.
    if count >= 10:
        losing_trial += 1
        print("\nYou've finished your trials\n")
        print("\tThe number is %d \n" % x)
        print("Better Luck Next time!\n")

    trials += 1
    
    return winning_trial, losing_trial, trials