from random import randrange
from typing import Text
import time

text = "MASTERMIND"
text2 = "Score Board"
records_name = []
records_turn = []
records_diff = []

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
        "By Gonzalo Requena Valero 1 DAW"
    )    
def menu():
    print(
        "\033[1;32;40m"
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
    # Difficulty = [large, value, repetition]
    # Easy -> Difficulty = [4, 5, False]
    #Middle-> Difficulty = [6, 7, False]
    # Hard -> Difficulty = [8, 9, True]
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
    print(
        "\t"
        ,"  Rules  ".center(30,"*")
        ,"\n"
        ,"\nThe object of MASTERMIND (r) is to guess a secret code.\nEach guest result in feedback narrowing down the possibilities\nof the code, and show the momentum tip.\nThe winner is the player who solves the code with fewer guesses."
    )
    time.sleep(100/50)
def game(difficulty):
    if difficulty[0] == 4:
        print("\nLets play!!! Easy mode on...\n")
    elif difficulty[0] == 6:
        print("\nLets play!!! Middle mode on...\n")
    else:
        print("\nLets play!!! Hard mode on...\n")
    name = input("\nEnter your user name: ")
    print("\nHellow",name,"\n")
    # Generate the password
    num = password_gen(difficulty)
    # while
    cont = 0
    tries_int = []
    
    while num != tries_int:
        n = ""
        tips = []
        tries = []
        tries_int = []
        mode = ""
        # Ask for it
        while len(n) != difficulty[0]:
            n = input("Guess the "+str(difficulty[0])+" digits number: ")
            cont += 1
        tries = list(n)
        
        for i in tries:
            tries_int.append(int(i))
        
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
        
        if num != tries_int:
            print("IA's answer:",tips,"\n")
    print("You're crowned",text,"!!! It only took",cont,"turns\n")

    # Return results "[name, turns, difficulty]"
    if difficulty[0] == 4:
        mode = "Easy mode"
    elif difficulty[0] == 6:
        mode = "Middle mode"
    else:
        mode = "Hard mode"
    records_name.append(name)
    records_turn.append(str(cont))
    records_diff.append(mode)
    return records_name, records_turn, records_diff 
def score_board():
    print()
    print(text2.center(40, "%"),"\n")
    print("Player:",records_name,"Turns:",records_turn,"Difficulty:",records_diff)
    return False

heading()

difficulty = [4, 5, False,"Easy"]

while True:
    time.sleep(2/1)
    menu()
    select = int(input("What are you going to do?\n"))
    
    if select == 1:        # Enter the game
        time.sleep(1)

        game(difficulty)
    elif select == 2:       # Choose difficulty
        time.sleep(1)

        difficulty = difficulty_select()
    elif select == 3:       # Show history records
        time.sleep(1)

        score_board()
        time.sleep(3)
        
    elif select == 4:       # Show rules
        time.sleep(1)

        rules()
    else:                   # Exit
        print("End of the game! Bye bye",text)
        time.sleep(4)
        break
