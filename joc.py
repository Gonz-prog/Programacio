#Joc que tirant una carta inferior a 12 i superior a 0 
#retorne sempre una superior.
#Qui arribe al 12 (rei) guanya


c=int(input("Tira la primera carta, vaig a guanyarte!!! "))
t=c

for i in range (t,13,1):
    
    if t==12:
        print("He guanyat perroo!!!")
    
    elif c==12:
        print("O has fet trampa o has guanyat animal de reguerot!!!")

    t=c+1
    
    print("Has tirat el ",c," de bastos i jo el ",t," de bastos.")

    c=int(input("Tira la primera carta, vaig a guanyarte!!! "))

else:
    print("No pots tirar ni per baix de 1 ni mes gran que 12 so samaruc")

    c=int(input("Tira altra carta, vull guanyarte samarro!!! "))