#https://www.geeksforgeeks.org/mastermind-game-using-python/

from random import randrange
from typing import Text

text = "MASTERMIND"

def menu():
    print(
        "\033[1;32;40m"
        "\n"
        +40*("_")
    )
    print(text.center(40, "_"))

    print(
        40*("*")
        +"\n"
    )
    print("Choices Menu\n")
    print()
    print("\nOption 1: Play the game")
    print("Option 2: Chose difficulty")
    print("Option 3: History Records")
    print("Anything to exit\n")
    print()
    return menu

menu()

while True:
    pass
