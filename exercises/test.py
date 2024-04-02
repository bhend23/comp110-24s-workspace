import random

# Define constants for emoji representations
WATER = "🟦"
BOAT = "🟥"
HIT = "🔴"
MISS = "⬜"

def input_guess(grid_size: int, guess_type: str) -> int:
    """
    Prompts the user for a row or column guess and returns the integer value.
    """
    assert guess_type == "row" or guess_type == "column", "Guess type must be 'row' or 'column'"
    
    valid_guess = False
    guess = 0
    while not valid_guess:
        guess = int(input(f"Guess a {guess_type}: "))
        if guess_type == "row":
            valid_guess = 1 <= guess <= grid_size
        else:
            valid_guess = 0 < guess <= grid_size
        if not valid_guess:
            print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    return guess

def print_grid(grid_size: int, row_guess: int, col_guess: int, correct: bool) -> None:
    """
    Prints the grid representation based on user's guesses and whether it's correct or not.
    """
    row = 1
    while row <= grid_size:
        col = 1
        while col <= grid_size:
            if row == row_guess and col == col_guess:
                if correct:
                    print(HIT, end="")
                else:
                    print(MISS, end="")
            else:
                print(WATER, end="")
            col += 1
        print()  # Move to the next line after printing a row
        row += 1

def correct_guess(secret_row: int, secret_col: int, guess_row: int, guess_col: int) -> bool:
    """
    Checks if the user's guess matches the secret boat location.
    """
    return secret_row == guess_row and secret_col == guess_col

def main(grid_size: int, secret_row: int, secret_col: int) -> None:
    """
    Main function controlling the game logic.
    """
    print(f"=== Turn 1/5 ===")
    turns = 1
    while turns <= 5:
        row_guess = input_guess(grid_size, "row")
        col_guess = input_guess(grid_size, "column")
        
        if correct_guess(secret_row, secret_col, row_guess, col_guess):
            print_grid(grid_size, row_guess, col_guess, correct=True)
            print("Hit!")
            print(f"You won in {turns}/5 turns!")
            return
        
        print_grid(grid_size, row_guess, col_guess, correct=False)
        print("Miss!")
        turns += 1
    
    print("X/5 - Better luck next time!")

if __name__ == "__main__":
    grid_size = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))