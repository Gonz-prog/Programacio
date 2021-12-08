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
def password_gen(difficulty):
    # Difficulty = [longitud, valores, repetición]
    # Fácil -> Difficulty = [4, 5, False]
    # Medio -> Difficulty = [6, 7, False]
    # Difícil -> Difficulty = [8, 9, True]
    password_list = []

    if difficulty[2] == False:
        for i in range(difficulty[0]):
            password = randrange(1,difficulty[1])
            while password in password_list:
                password = randrange(1,difficulty[1])
            password_list.append(password)

    else:
        for i in range(difficulty[0]):
            password = randrange(1,difficulty[1])
            password_list.append(password)
    return password_list
def difficulty_select():            # Create difficulty list
    diff = 0
    while diff not in [1, 2, 3]:
        print("Choose an option!\n")
        print("1: Easy\n")
        print("2: Middle\n")
        print("3: Hard\n")
        diff = int(input("Selection: "))
        
    if diff == 1:
        difficulty = [4, 5, False,"Easy"]
    elif diff == 2:
        difficulty = [6, 7, False,"Middle"]
    else:
        difficulty = [8, 9, True,"Hard"]
    return difficulty
def rules():
    print("Rules".center(20,"*"),"\n")
    return False
def game():
    name = input("\nEnter your user name\n")
    print("Hellow",name,"\n")
    # Generate the password
    num = password_gen(difficulty)
    # while
    tries = []
    tips = []
    tries_int = []
    n = ""
    while num != tries:
        # Ask for it
        while len(n) != difficulty[0]:
            n = input("Guess the "+str(difficulty[0])+" digits number "+name+": ")
        tries = list(n)
        for i in tries:
            tries_int.append(int(i))
        print(num)
        print(tries_int)
        # Compare them and show the tips
        for (i,k) in zip(num,tries_int):
            if i == int(k):
                tips.append("*")
            elif i != int(k) and int(k) in num:
                tips.append("_")
            elif i != int(k) and int(k) not in num:
                tips.append(" ")
        # Show results
        print("Your answer:",tries,"\n")
        print("IA's answer:",tips,"\n")
    print("You're",text,"!!!\n")

    # Return results "[name, turns, difficulty]"

heading()
difficulty = [4, 5, False,"Easy"]

while True:
    
    menu()
    select = int(input("What are you going to do?\n"))
    
    if select == 1:         # Enter the game
        game()
    elif select == 2:       # Choose difficulty
        difficulty = difficulty_select()
    elif select == 3:       # Show history records
        pass
    elif select == 4:       # Show rules
        rules()
    else:                   # Exit
        print("End of the game")
        break
