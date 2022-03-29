"""A number-guessing game."""
import random

name = input("Howdy, what's your name? ")
print(name + ", I'm thinking of a number between 1 and 100.")
secret_number = random.randint(1, 100)
guess = None

while secret_number != guess:
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
print("You guessed right!")