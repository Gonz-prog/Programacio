from random import randrange
from typing import Text

text = "MASTERMIND"
def heading():
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
def menu():
    print(
        "\033[1;32;40m"
        "\n"
        +40*("_")
    )
    print(
        40*("*")
        +"\n"
    )
    print("Choices Menu\n")
    print()
    print("\nOption 1: Play the game")
    print("Option 2: Chose difficulty")
    print("Option 3: History Records")
    print("Option 4: Rules")
    print("Anything to exit\n")
    print()   
def password_gen(select,easy,middle,difficult):
    
    easy_list = []
    middle_list = []
    difficult_list = []

    easy = 4
    middle = 6
    difficult = 8

    if select == "lvl1":
        for i in range(easy):
            num = randrange(1,6)
            while num in easy_list:
                num = randrange(1,6)
        easy_list.append(num)
        return easy_list

    if select == "lvl2":
        for i in range(middle):
            num = randrange(1,9)
            while num in middle_list:
                num = randrange(1,6)
        middle_list.append(num)
        return middle_list

    if select == "lvl3":
        for i in range(difficult):
            num = randrange(1,9)    
        difficult_list.append(num)
        return difficult_list
def user():
    name = input("\nEnter your user name\n")
    print("Hellow",name,"\n")
    return False
def rules():
    print("Rules".center(20,"*"),"\n")
    return False

heading()
user()
while True:
    menu()
    select = int(input("What are you going to do?\n"))
    
    if select == 4:
        rules()
