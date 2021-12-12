from random import randrange
from typing import Text
import time
import os                                                 
text = " MASTERMIND "                                           # This is the str we use to show the results
text2 = " Score Board "                                         # This is the str we use to show the score board
text3 = "                 Gonzalo Requena Valero"               
text4 = "      IES Jaume II el Just Tavernes de la Valldigna"   # There are the str to be shown with the heading
text5 = "                         1 DAW"                                              
select = 0
records_name = []                   
records_turn = []                                               # Those lists we introduce here are used to store the player(s) data
records_diff = []                   
def heading():                                                  # This is the game's heading
    print(60*("_"))
    print(text.center(60, "_"))
    print(
        60*("*")
        +"\n",text4
        +"\n",text3
        +"\n",text5
    )    
def menu():                                                     # Menu function
    print(
        +60*("_")
    )
    print(
        60*("*")
        +"\n"
    )
    print("Player Options\n")
    print()
    print("\n 1: Play the game\t\t->\t",difficulty[3])
    print(" 2: Chose difficulty")
    print(" 3: History Records")
    print(" 4: Rules")
    print(" 5: Exit\n")
    print()
def password_gen(difficulty):                                   # This is the password generator, it will give each game's secret password in each level of difficulty
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
def difficulty_select():                                        # Create difficulty list to import the value of each difficulty
    diff = 0
    while diff not in [1, 2, 3]:
        print("\nChoose a game mode!\n")
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
def rules():                                                    # This funtion prints the rules of the game
    print(
        "\t"
        ,"  Rules  ".center(55,"*")
        ,"\n"
        ,"\nThe object of MASTERMIND (r) is to guess a secret code.\nEach guest result in feedback narrowing down the possibilities\nof the code, and show the momentum tip.\nThe winner is the player who solves the code with fewer guesses."
    )
    time.sleep(10)
def game(difficulty):                                           # This is the main function, wich recives the difficulty list to play in the asumed level. Then returns three list with the name, turn(s) and difficulty
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
        cont += 1
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
def score_board():                                              # This function shows the score board when recive the three list already mentioned
    print()
    print(text2.center(58, "%"),"\n")
    for (x,y,z) in zip(records_name,records_turn,records_diff):
        print("Player:",x.ljust(10),"Turn(s):",y.ljust(5),"Difficulty:",z)
    return False
difficulty = [4, 5, False,"Easy"]                               # Variable to set the difficulty to its default on easy mode
while True:                                                     # Main Loop
    print("\033[1;32;40m")                                      # Color introduction          
    os.system("clear")                                          # System function used to clear the window
    time.sleep(1)                                               # Time stops to create a retro game environment
    heading()                                                   # Heading call               
    menu()                                                      # Menu call
    select = (input("Chose an option\n"))
    while select not in [1,2,3,4,5] and select.isnumeric() == False:
        select = (input("Invalid option. Try again\n"))      # Main loop input (Menu option chosen)
    if int(select) == 1:                                             # Enter the game
        time.sleep(1)
        os.system("clear")
        game(difficulty)
        time.sleep(3)                                           # Gam call
    elif int(select) == 2:                                           # Choose difficulty
        time.sleep(1)
        os.system("clear")
        difficulty = difficulty_select()                        # Difficulty select menu call
        os.system("clear")
    elif int(select) == 3:                                           # Show history records
        time.sleep(1)
        os.system("clear")
        score_board()                                           # Score Board call
        time.sleep(3)
        os.system("clear")
    elif int(select) == 4:                                           # Show rules
        time.sleep(1)
        os.system("clear")
        rules()                                                 # Rules call
        os.system("clear")
    else:                                                       # Exit
        os.system("clear") 
        print("End of the game! Bye bye",text)
        time.sleep(4)
        os.system("clear")
        break                                                   # Main loop breakdow
