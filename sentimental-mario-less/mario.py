# TODO
from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:  # Height must be between 1 - 8
        break


# Create new line until reach height
for row in range(0, height, 1):  # range(start, stop, step)
    # Add spaces before for each hash until height - 1. (Space = height - Line - 1)
    for col in range(0, height, 1):  # range(start, stop, step)
        if row + col < height - 1:
            print(" ", end="")
        else:
            # Add hashes
            print("#", end="")
    print()
