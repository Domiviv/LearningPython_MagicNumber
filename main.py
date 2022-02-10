import random


def ask_number(min, max):
    number = 0
    while number == 0:
        s = input(f"What is the magic number? (between {min} and {max}) ")
        try:
            number = int(s)
        except ValueError:
            print(f"ERROR: {s} is not a number. Please try again.")
        else:
            if number < min or number > max:
                print(f"ERROR: Please, enter a number between {min} and {max}")
                number = 0
    return number


MAX = 10
MIN = 1
MAGIC_NUMBER = random.randint(MIN, MAX)
nb = 0

while not nb == MAGIC_NUMBER:
    nb = ask_number(MIN, MAX)
    if nb == MAGIC_NUMBER:
        print(f"Congratulations, the magic number was {MAGIC_NUMBER}")
    elif nb > MAGIC_NUMBER:
        print(f"Oops, the number you are looking for is smaller")
    elif nb < MAGIC_NUMBER:
        print(f"Oops, the number you are looking for is greater")



