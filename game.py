"""A number-guessing game."""
"""
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
"""

import random

name = input("Howdy, what's your name? ")
print(name + ", I'm thinking of a number between 1 and 100.")
secret_number = random.randint(1, 100)
guess = None
count = 0

while secret_number != guess: 
    try:   
        guess = int(input("Try to guess my number: "))    
        print("Your guess? " + str(guess))
        if int(guess) > 100:
            print("Make sure your guess is between 1-100!")
        if int(guess) < 1:
            print ("Make sure your guess is between 1-100!")
        if int(guess) > secret_number:
            print("Your guessed number is too high!")        
        if int(guess) < secret_number:
            print("You guessed number is too low! ") 
        count = count + 1               
    except ValueError:
        print("Please print a number!")
print("Nice job, " + name + "! You guessed it in " + str(count) + " tries!")