from random import randrange
print("\n\033[1;32;40m Bright Green  \n")
rando = randrange(0,7)
num = int(input("Choose a 4-8 digit number\n"))

def win():
    if rando == num:
        print("Crowned, You're the MASTERMIND\n")
    else:
        print("\nNice try\n")
    return win

def bad_choice():
    if num <4 or num >9:
        print("\nWrong number!\n")
    return bad_choice

win()
bad_choice()
