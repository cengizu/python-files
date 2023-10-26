# Crack a 4 digit of alphabet password

from string import ascii_letters
from itertools import product

for passcode in product(ascii_letters, repeat=4):
    print(*passcode)
