"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730664108"

user_input: str = input("Pick a secret boat location between 1 and 4: ")

user_number: int = int(user_input)

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# user_number is above 4, make error
if user_number > 4:
    print(f"Error! {user_input} too high!")
    exit()

# user_number is below 1, make error
if user_number < 1:
    print(f"Error! {user_input} too low!")
    exit()

# guess_number correct or incorrect
user_guess: str = input("Guess a number between 1 and 4: ")
guess_number: int = int(user_guess)
if guess_number == user_number:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")


# emoji string correct
    
emoji_string = ""

if guess_number == 1:
    emoji_string += RED_BOX if guess_number == user_number else WHITE_BOX
else:
    emoji_string += BLUE_BOX

if guess_number == 2:
    emoji_string += RED_BOX if guess_number == user_number else WHITE_BOX
else:
    emoji_string += BLUE_BOX

if guess_number == 3:
    emoji_string += RED_BOX if guess_number == user_number else WHITE_BOX
else:
    emoji_string += BLUE_BOX

if guess_number == 4:
    emoji_string += RED_BOX if guess_number == user_number else WHITE_BOX
else:
    emoji_string += BLUE_BOX

print(emoji_string)
exit()