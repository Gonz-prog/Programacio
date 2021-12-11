from random import *
from os import *
from time import *

def define_difficulty():
    option=(input("\nSelect the difficulty level [ password lenght, numbers available, repetition ]:\n\n->\t1. Easy\t\t[ 4, 5, No ]\n->\t2. Normal\t[ 6, 7, No ]\n->\t3. Hard\t\t[ 8, 9, Yes ]\n\nSelection:  "))
    while option.isnumeric()==False and option not in [1,2,3]:                    # mentre l'usuari no seleccione un valor valid, continuem preguntant
        system('cls')
        option=(input("Invalid Input".center(90,"_")+"\n\nSelect the difficulty level [ password lenght, numbers available, repetition ]:\n\n->\t1. Easy\t\t[ 4, 5, No ]\n->\t2. Normal\t[ 6, 7, No ]\n->\t3. Hard\t\t[ 8, 9, Yes ]\n\nSelection:  "))
    option=int(option)
    if option==1:
        mode=[4,5,False,"Easy"]                           # password facil: [4 valors, 5 nombres, sense repeticio]
    elif option==2:
        mode=[6,7,False,"Middle"]                          # password mig: [6 valors, 7 nombres, sense repeticio]
    else:
        mode=[8,9,True,"Hard"]                          # password dificil: [8 valors, 9 nombres, amb repeticio]
    print("\nSelected",mode[3],"mode")
    clear()
    return mode

def define_password():
    password=[]                                     # declarem la llista de la contrasenya
    for i in range(0,mode[0]):                      # recorrem les posicions de la llista
        valor=choice(range(1,mode[1]))            # escollim un valor al atzar entre 1 i el nombre maxim disponible (+1 per com funciona la funcio)
        if mode[2] == False:                        # si la repeticio esta desactivada, es a dir, facil / intermig
            while valor in password:                # mentre el valor generat ja es trove en la llista (sense repeticio)
                valor=choice(range(1,mode[1]))    # genera un valor nou
        else:                                       # si la repeticio esta desactivada
            pass                                    # tots els valors son valids, no fem res mes
        password.append(valor)                      # una vegada tinga un valor que no es trove en la llista, afegeix-lo
    return password

def play():
    code,tries=[],0
    name=input("Dona'm el teu alias per a la partida: ")
    password=define_password()    
    while True:
        tries+=1
        code,tips=[],[]
        while len(code)!=mode[0]:
            code=list(input("\nDona'm la teva jugada["+str(mode[0])+" xifres]:  "))
        for (passw,answer) in zip(password,code):
            if passw==int(answer):
                tips.append("*")
            elif int(answer) in password:
                tips.append("_")
            else:
                tips.append(" ")
        if tips.count("*") == mode[0]:
            break
        if len(name)>4: print("\nJugada de "+name+":\t",code,"\nPistas del CPU:\t\t",tips)
        else: print("\nJugada de "+name+":\t\t",code,"\nPistas del CPU:\t\t",tips)
    print("\nEnhorabuena, "+name+" has ganado en",tries,"turnos!\n")
    score=[mode[3],name,tries]
    scoreboard[score[0]][score[1]] = score[2]
    clear()

def menu():
    print("Menu".center(90,"_")+"\n\n"+"1. Play[".rjust(44)+mode[3]+" mode]\n"+"2. Select difficulty\n".rjust(57)+"3. Show settings\n".rjust(53)+"4. Show scoreboard\n".rjust(55)+"5. Exit\n".rjust(48))
    seleccion=int(input("\nSelect an option: "))
    while seleccion not in [1,2,3,4,5]:
        seleccion=int(input("\n\nPlease, choose a valid option: "))
    system('cls')
    return seleccion

def print_scoreboard():
    for (lvl,difficulty) in zip(scoreboard.keys(),scoreboard.values()):
        first,second,third=0,0,0
        first_pos,second_pos,third_pos="NaN","NaN","NaN"
        for (player,points) in zip(difficulty.keys(),difficulty.values()):
            if points<first or first==0:
                first,second,third=points,first,second
                first_pos,second_pos,third_pos=player+" - "+str(points)+" turnos",first_pos,second_pos
            elif points<second or second==0:
                second,third=points,second
                second_pos,third_pos=player+" - "+str(points)+" turnos",second_pos
            elif points<third or third==0:
                third=points
                third_pos=player+" - "+str(points)+" turnos"
        print("\n\n"+("Top 3 players mode "+lvl).center(95,"_")+"\n\n\t"+("1st. "+first_pos).center(80)+"\n\t"+("2nd. "+second_pos).center(80)+"\n\t"+("3rd. "+third_pos).center(80))
    clear()

def clear():
    input("\n\nPress any key to return to the menu ")
    print("\nLoading",end=""),sleep(1/2),print(".",end="",flush=True),sleep(1),print(".",end="",flush=True),sleep(1),print(".",end="",flush=True),sleep(1/2)
    system("cls")

mode=[4,5,False,"Easy"]
scoreboard={
    "Easy":{},
    "Middle":{},
    "Hard":{}
}

system('cls')
while True:
    seleccion=menu()

    if seleccion == 1:                  # 1 -> play
        play()
    elif seleccion == 2:                # 2 -> difficulty
        mode=define_difficulty()
    elif seleccion == 3:                # 3 -> show settings
        system('cls')
        print("\n"+mode[3]+":\n\t1. Longitud del password:",mode[0],"\n\t2. Números disponibles:",list(range(mode[1]+1)),"\n\t3. Repetición:",mode[2])
        clear()
    elif seleccion == 4:                # 4 -> print scoreborad
        print_scoreboard()
    elif seleccion == 5:                # 5 -> exit
        print("\nShuting down",end="",flush=True),sleep(1/2),print(".",end="",flush=True),sleep(1),print(".",end="",flush=True),sleep(1),print(". ",end="",flush=True),sleep(1)
        system('cls')
        break
