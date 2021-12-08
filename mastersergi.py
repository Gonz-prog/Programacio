from random import choice

# Functions

    # Funcio que ens permet seleccionar el nivell de dificultat i retorna una llista amb els parameters del password
def difficulty_choice():
    # demanem un enter per a seleccionar el nivell de dificultat
    option=int(input("\nSelecciona el modo de juego:\n\n->\tFácil[1]\n->\tNormal[2]\n->\tDifícil[3]\n\nSelección:\t"))
    while option not in [1,2,3]:                    # mentre l'usuari no seleccione un valor valid, continuem preguntant
        option=int(input("\nSelecciona el modo de juego:\n\n->\tFácil[1]\n\t->Normal[2]\n->\tDifícil[3]\n\nSelección:\t"))
    if option==1:
        modo,difficulty=[4,5,False],"Fácil"                           # password facil: [4 valors, 5 nombres, sense repeticio]
    elif option==2:
        modo,difficulty=[6,7,False],"Normal"                          # password mig: [6 valors, 7 nombres, sense repeticio]
    elif option==3:
        modo,difficulty=[8,9,True],"Difícil"                          # password dificil: [8 valors, 9 nombres, amb repeticio]
    return modo,difficulty                                            # retornem els parameteres a la funcio principal

    # Funcio que genera una contrasenya segons el nivell de dificultat
def password_gen(mode):     # la dificultat ve donada en una llista amb l'estructura [longitud de la contrasenya, nº de nombres utilitzats, repeticio(boolean)]
    password=[]                                     # declarem la llista de la contrasenya
    for i in range(0,mode[0]):                      # recorrem les posicions de la llista
        valor=choice(range(1,mode[1]+1))            # escollim un valor al atzar entre 1 i el nombre maxim disponible (+1 per com funciona la funcio)
        if mode[2] == False:                        # si la repeticio esta desactivada, es a dir, facil / intermig
            while valor in password:                # mentre el valor generat ja es trove en la llista (sense repeticio)
                valor=choice(range(1,mode[1]+1))    # genera un valor nou
        else:                                       # si la repeticio esta desactivada
            pass                                    # tots els valors son valids, no fem res mes
        password.append(valor)                      # una vegada tinga un valor que no es trove en la llista, afegeix-lo
    return password                                 # una vegada hem recorregut i plenat tota la llista, la retornem al programa principal

    # Funcio que generara el menu i retornara la seleccio del usuari
def menu():
    # imprimim el menu per pantalla i arrepleguem un enter com a la seleccio del usuari
    print("\nSelecciona una opción:\n\t1. Jugar\t-->\t"+difficulty+"\n\t2. Opciones de dificultad\n\t3. Mostrar los parámetros del nivel de dificultad\n\t4. Mostrar tabla de puntuaciones\n\t5. Salir")
    seleccion=int(input("Elije una opción: "))
    while seleccion not in [1,2,3,4]:               # mentre el usuari no seleccione un valor valid, continua preguntant
        seleccion=int(input("Por favor, elije una opción válida: "))
    return seleccion                                # una vegada validat, retorna el valor de a seleccio
    # Funcio que executa la partida utilitzant les funcions previes
def play(mode):

    intentos=0
    codigo=[]
    pistas=[]
    name=input("Donam el teu alias per a la partida: ")
    password=password_gen(mode)

    while password != codigo:

        intentos += 1
        codigo=[]
        pistas=[]

        for i in range(mode[0]):
            codigo.append(int(input("\nDame el valor nº"+str(i+1)+" del codigo:")))
            
            if codigo[i] == password[i]:
                pistas.append("*")
            elif codigo[i] in password:
                pistas.append("_")
            else:
                pistas.append("' '")

        print("Jugada de",name,":\t\t",end="")
        for i in range(mode[0]):
            print(codigo[i],end=" ")
        print("\nPistas ofrecidas:\t",end="")
        for i in range(mode[0]):
            print(pistas[i],end=" ")

    print("Enhorabuena,",name,"has ganado en",intentos,"turnos!")
    result=tuple(name,intentos)
    return result
def print_settings(mode):
    if mode[0] == 4:
        difficulty,repeticion="Fácil","no"
    elif mode[0] == 6:
        difficulty,repeticion="Normal","no"
    elif mode[0] == 8:
        difficulty,repeticion="Difícil","si"
    print("\n"+difficulty+":\n\t1. Longitud del password:",mode[0],"\n\t2. Números disponibles:",list(range(mode[1]+1)),"\n\t3. Repetición:",repeticion)

# Variables
mode=[4,5,False]                        # easy by default
difficulty="Fácil"
scoreboard={}

# Main loop
while True:

    seleccion=menu()

    if seleccion == 1:                  # 1 -> play
        score=play(mode)
        if score[0] in scoreboard.keys() and score[1]>scoreboard[score[0]]:
            continue
        else:
            scoreboard[score[0]] = difficulty+": "+str(score[1])+" turnos"
    elif seleccion == 2:                # 2 -> difficulty
... (13 líneas restantes)
