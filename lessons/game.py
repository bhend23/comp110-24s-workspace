"""Number guessing game."""
from random import randint

SECRET: int = randint(1,10)
correct: bool = False


while correct == False: # also can be not correct
    guess: int = int(input("Guess a number: "))

    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number!")
        correct = True
    elif guess > SECRET:
        print("Your guess is too high!")
        print("Try again!")
        