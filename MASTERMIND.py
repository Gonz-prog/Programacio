#https://www.geeksforgeeks.org/mastermind-game-using-python/

from random import randrange

rando =  randrange(1,7)

text="MASTERMIND"
print(
    "\n"
    +40*("_")
)
print(text.center(40, "_"))

print(
    40*("*")
    ,"\n"
)

def menu():
    print("Choices Menu\n")
    print("^(*_/_*)^")
    print("\nOption 1: Play the game")
    print("Option 2: Chose difficulty")
    print("Option 3: History Records")
    print("Anything to exit\n")
    print()

    return menu

menu()

num = int(input("Choose a 4-8 digit number\n"))

def prove():
    if rando == num:
        print("Crowned, You're the MASTERMIND")
    elif num <=4 or num >=9:
        print("Wrong number!\n")
