# Crack a 4 digit password with alphanumeric and punctuation

from string import ascii_letters, digits, punctuation
from itertools import product

for passcode in product(ascii_letters + digits + punctuation, repeat=4):
    print(*passcode)
