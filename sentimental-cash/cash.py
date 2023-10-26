# TODO
from cs50 import get_float

while True:
    cash = get_float("Change owed: ")
    if cash > 0:
        cent = round(cash * 100)
        coins = 0

        quarters = 0
        dimes = 0
        nickels = 0
        pennies = 0

        # Calulate quarters
        quarters = int(cent / 25)
        # Calulate dime
        dimes = int((cent % 25) / 10)
        # Calulate nickels
        nickels = int(((cent % 25) % 10) / 5)
        # Calulate pennies
        pennies = int(((cent % 25) % 10) % 5)

        coins += quarters + dimes + nickels + pennies

        print(coins)
        break
