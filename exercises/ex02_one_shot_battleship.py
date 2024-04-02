"""One shot battleship."""

__author__ = "730664108"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2
not_range_check = False
in_range_check = True

while not not_range_check:
    user_row: str = input("Guess a row: ")
    user_row = int(user_row)
    if user_row < 1 or user_row > grid_size:
        try_again_row: str = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
        user_row = int(try_again_row)
    user_column: str = input("Guess a column: ")
    user_column = int(user_column)
    if user_column < 1 or user_column > grid_size:
        try_again_col: str = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
        user_column = int(try_again_col)
    if user_column >= 1 and user_column <= grid_size and user_row >= 1 and user_row <= grid_size:
        not_range_check = True

        
while in_range_check is True:
    if secret_row == user_row and secret_column == user_column:
        in_range_check = False
    elif user_column and user_row <= grid_size:
        in_range_check = False

# Grid red, blue, and white boxes

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# GRID STRING ROW 1
grid_string1: str = ""

if user_row == 1 and user_column == 1:
    grid_string1 += RED_BOX if user_row == secret_row and user_column == secret_column else WHITE_BOX
else:
    grid_string1 += BLUE_BOX
if user_row == 1 and user_column == 2:
    grid_string1 += RED_BOX if user_row == secret_row and user_column == secret_column else WHITE_BOX
else:
    grid_string1 += BLUE_BOX
if user_row == 1 and user_column == 3:
    grid_string1 += RED_BOX if user_row == secret_row and user_column == secret_column else WHITE_BOX
else:
    grid_string1 += BLUE_BOX
if user_row == 1 and user_column == 4:
    grid_string1 += RED_BOX if user_row == secret_row and user_column == secret_column else WHITE_BOX
else:
    grid_string1 += BLUE_BOX

print(grid_string1)

# GRID STRING ROW 2
grid_string2: str = ""

if user_row == 2 and user_column == 1:
    grid_string2 += RED_BOX if user_row == secret_row and user_column == secret_column else WHITE_BOX
else:
    grid_string2 += BLUE_BOX
if user_row == 2 and user_column == 2:
    grid_string2 += RED_BOX if user_row == secret_row and user_column == secret_column else WHITE_BOX
else:
    grid_string2 += BLUE_BOX
if user_row == 2 and user_column == 3:
    grid_string2 += RED_BOX if user_row == secret_row and user_column == secret_column else WHITE_BOX
else:
    grid_string2 += BLUE_BOX
if user_row == 2 and user_column == 4:
    grid_string2 += RED_BOX if user_row == secret_row and user_column == secret_column else WHITE_BOX
else:
    grid_string2 += BLUE_BOX

print(grid_string2)

# GRID STRING ROW 3
grid_string3: str = ""

if user_row == 3 and user_column == 1:
    grid_string3 += RED_BOX if user_row == secret_row and user_column == secret_column else WHITE_BOX
else:
    grid_string3 += BLUE_BOX
if user_row == 3 and user_column == 2:
    grid_string3 += RED_BOX if user_row == secret_row and user_column == secret_column else WHITE_BOX
else:
    grid_string3 += BLUE_BOX
if user_row == 3 and user_column == 3:
    grid_string3 += RED_BOX if user_row == secret_row and user_column == secret_column else WHITE_BOX
else:
    grid_string3 += BLUE_BOX
if user_row == 3 and user_column == 4:
    grid_string3 += RED_BOX if user_row == secret_row and user_column == secret_column else WHITE_BOX
else:
    grid_string3 += BLUE_BOX

print(grid_string3)

# GRID STRING ROW 4
grid_string4: str = ""

if user_row == 4 and user_column == 1:
    grid_string4 += RED_BOX if user_row == secret_row and user_column == secret_column else WHITE_BOX
else:
    grid_string4 += BLUE_BOX
if user_row == 4 and user_column == 2:
    grid_string4 += RED_BOX if user_row == secret_row and user_column == secret_column else WHITE_BOX
else:
    grid_string4 += BLUE_BOX
if user_row == 4 and user_column == 3:
    grid_string4 += RED_BOX if user_row == secret_row and user_column == secret_column else WHITE_BOX
else:
    grid_string4 += BLUE_BOX
if user_row == 4 and user_column == 4:
    grid_string4 += RED_BOX if user_row == secret_row and user_column == secret_column else WHITE_BOX
else:
    grid_string4 += BLUE_BOX

print(grid_string4)

# Print miss or hit
if not_range_check is True:
    if user_column == secret_column and user_row != secret_row:
        print("Close! Correct column, wrong row.")
    if user_row == secret_row and user_column != secret_column:
        print("Close! Correct row, wrong column.")
    elif secret_row == user_row and secret_column == user_column:
        print("Hit!")
    elif user_column <= grid_size or user_row <= grid_size:
        print("Miss!")