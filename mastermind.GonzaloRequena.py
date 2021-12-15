from random import randrange
from typing import Text
from time import sleep
from os import system                                            

text = "MASTERMIND"
records_name = []                   
records_turn = []                                               
records_diff = []
difficulty = [4, 5, False,"Easy"]                               # Variable to set the difficulty to its default value on easy mode

def win():                                                      # Title to be shown when the player(s) win(s) a game
    print(" ___  ___      ______     ____  ____       __   __  ___   __      _____  ___ ")
    print("|:  \/:  |    /    : \   (:  _||_ : |     |:  |/  \|  :| |: \    (\:   \|:  \ ") 
    print(" \   \  /    // ____  \  |   (  ) : |     |'  /    \:  | ||  |   |.\\    \    | ") 
    print("  \\   \/    /  /    ) :) (:  |  | . )    \\: /'         | |:  |   |: \.    \\  | ")
    print("  /   /    (: (____/ //  \\   \__/ //      \ // /\'      | |.  |   |.  \    \. | ")
    print(" /   /      \       /    /\\  __  //\      /   /  \\     | /\  |\  |    \    \ | ")
    print("|___/        \"_____/    (__________)     |___/    \___ |(__\_|_) \___|\_____\) ")
    print()
def heading():                                                  # This is the game's heading
    system("clear")                                                  
    print()
    print(" ___      ___       __        ________  ___________  _______   ______   ___      ___   __    _____  ___   ________")
    print("|   \    /   |     /  \      /        )(      _    )       | /       \ |   \    /   | |  \  (\    \|   \ |        |") 
    print(" \   \  //   |    /    \    (:   \___/  )__/  \\__/(: ______)|:        | \   \  //   | ||  | |.\\   \    |(.   ___  :)")
    print(" /\\   \/.    |   /' /\  \    \___  \       \\_ /    \/    |  |_____/   ) /\\   \/.    | |:  | |: \.   \\  ||:  \   ) ||") 
    print("|: \.        |  //  __'  \    __/  \\      |.  |    // ___)_  //      / |: \.        | |.  | |.  \    \. |(| (___\ ||")
    print("|.  \    /:  | /   /  \\  \  /* \   :)     \:  |   (:      *||:  __   \ |.  \    /:  | /\  |\|    \    \ ||:       :)") 
    print("|___|\__/|___|(___/    \___)_______/       \__|    \_______)|__|  \___)|___|\__/|___|(__\_|_)\___|\____\)(________/")
    print("\n")       
def menu():                                                     # Menu function
    heading()
    print("\n 1: Play the game\tMode-->\t",difficulty[3])
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
    heading()
    diff = ''
    while diff not in [1, 2, 3] and diff.isnumeric() == False:
        print("\nChoose a game mode!\n")
        print("1: Easy\n")
        print("2: Middle\n")
        print("3: Hard\n")
        diff = (input("Selection: "))
    if int(diff) == 1:
        difficulty = [4, 5, False,"Easy"]
    elif int(diff) == 2:
        difficulty = [6, 7, False,"Middle"]
    else:
        difficulty = [8, 9, True,"Hard"]
    clean()
    return difficulty
def rules():                                                    # This funtion prints the rules of the game
    print("  _______    ____  ____   ___         _______    ________  ")
    print(" /:      \  (:  _||_ : | |:  |       /:     :|  \:       ) ") 
    print("|:        | |   (  ) : | ||  |      (: ______) (:   \___/ ")  
    print("|_____/   ) (:  |  | . ) |:  |       \/    |    \___  \    ")
    print("//       /  \\   \__/  //  \  |___    // ___)_    __/   \\   ")
    print(" |:  __   \  \\   __   //   \_|:  \  (:      :|  /: \   :)  ")
    print(" |__|  \___)  (_______)  \________\  \_______) (_______/")
    print(
        "\n"
        ,"\nThe object of MASTERMIND (r) is to guess a secret code.\nEach guest result in feedback narrowing down the possibilities\nof the code, and show the momentum tip.\nThe winner is the player who solves the code with fewer guesses.")
    clean()   
def game(difficulty):                                           # This is the main function, wich recives the difficulty list to play in the asumed level. Then returns three list with the name, turn(s) and difficulty
    print(" ___         _______   ___________    ____    ________         _______    ___             __       ___  ___  ")
    print("|.  |       /:     .| (:     _   .)  ))_ :)  /.       )       |   __ :\  |.  |           /:.\     |:  \/.  | ")
    print("||  |      (: ______)  )__/  \\ __/  (____(  (:   \___/        (. |__) :) ||  |          /    \     \   \  /  ")
    print("|:  |       \/    |       \\ _ /              \___  \          |:  ____/  |:  |         /' /\  \     \\   \/   ")
    print(" \  |___    // ___)_      |.  |               __/  \\          (|  /       \  |___     //  __'  \    /   /    ")
    print("( \_|:  \  (:      .|     \:  |              /. \   :)       /|__/ \     ( \_|:  \   /   /  \\   \  /   /     ")
    print(" \_______)  \_______)      \__|             (_______/       (_______)     \_______) (___/    \___)|___/      ")
    print()
    if difficulty[0] == 4:
        print("\nEasy mode on...\n")
    elif difficulty[0] == 6:
        print("\nMiddle mode on...\n")
    else:
        print("\nHard mode on...\n")
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
        cont += 1                                               # Count the turn as a variable
        print("Your answer:",tries,"\n")
        if num != tries_int:
            print("IA's answer:",tips,"\n")
    win()
    print("\nYou're crowned",text,"!!! It only took",cont,"turns\n")
    clean()
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
    print("  ________    ______       ______      _______     _______       _______       ______          __        _______    ________   ")
    print(" /:       )  /: _  :\     /      \    /:      \   /.     :|     |   _  .\     /    . \        /:.\      /.      \  |:      .\ ") 
    print("(:   \___/  (: ( \___)   // ____  \  |:        | (: ______)     (. |_)  :)   // ____  \      /    \    |:        | (.  ___  :)") 
    print(" \___  \     \/ (       /  /    ) :) |_____/   )  \/    |       |:     \/   /  /    ) :)    /' /\  \   |_____/   ) |: \   ) ||") 
    print("  __/   \\    // (  _   (: (____/ //   //      /   // ___)_      (|  _  \\   (: (____/ //    //  __'  \   //      /  (| (___\ ||") 
    print(" /. \   :)  (:   _) \   \        /   |:  __   \  (:      .|     |: |_)  :)  \        /    /   /   \\  \ |:  __   \  |:       :)")
    print("(_______/    \_______)   \._____/    |__|  \___)  \_______)     (_______/    \._____/    (___/    \___)|__|  \___) (________/")
    print("\n")
    for (x,y,z) in zip(records_name,records_turn,records_diff):
        print("Player:",x.ljust(10),"Turn(s):",y.ljust(5),"Difficulty:",z)
    clean()
    return False
def clean():
    input("\nPress enter to return to the menu ")
    print("\nGoing back")
while True:                                                     # Main Loop                                                      
    print("\033[1;32;40m")                                      # Text color introduction 
    system("clear")                                             # System function used to clear the window
    sleep(1)                                                    # Make the system sleep for a second to generate the retro gaming atmosphere
    menu()                                                      # Menu call
    select = (input("Choose an option\n"))                      # Main loop input (Menu option chosen)
    while select not in [1,2,3,4,5] and select.isnumeric() == False:                
        system("clear")                                          
        sleep(1)                                                                                                                
        menu()                                                      
        select = (input("Choose an option\n"))      
    sleep(1)
    system("clear")
    if int(select) == 1:                                        # Enter the game
        game(difficulty)                                        # Game call                                                
    elif int(select) == 2:                                      # Choose difficulty
        difficulty = difficulty_select()                        # Difficulty select menu call
    elif int(select) == 3:                                      # Show history records
        score_board()                                           # Score Board call
    elif int(select) == 4:                                      # Show rules
        rules()                                                 # Rules call
    else:                                                       # Exit 
        print("End of the game! Bye bye",text)
        sleep(4)
        system("clear")
        break
