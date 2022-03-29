"""A number-guessing game."""
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
        if guess > 100 or guess < 1:
            print("Make sure your guess is between 1-100!")        
        if guess > secret_number and guess < 101:
            print("Your guessed number is too high!")        
        if guess < secret_number and guess > 0:
            print("You guessed number is too low! ") 
        count = count + 1               
    except ValueError:
        print("Please print a number!")
print("Nice job, " + name + "! You guessed it in " + str(count) + " tries!")