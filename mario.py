
"""while True:
    n = get_int("Height: ")
    if n > 0:
        break

for i in range(n):
    print("#")"""

"""def main():
    height = get_height()
    for i in range(height):
        print("#")


def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                return n
        except ValueError:
            print("Not a number.")

main()"""

for row in range(3):
    print("#" * 3)
