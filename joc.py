
#Joc que tirant una carta inferior a 12 i superior a 0 
#retorne sempre una superior.
#Qui arribe al 12 guanya


c=int(input("Tira la primera carta, vaig a guanyarte!!! "))

t=c+1

while c<=0 or c>=13:

    print("No pots tirar ni per baix de 1 ni mes gran que 12 so samaruc")

    c=int(input("Tira altra carta, vull guanyarte samarro!!! "))

while c<=11 and t<=11:

    print("Has tirat el ",c," de bastos i jo el ",t," de bastos.")

    c=int(input("Tira altra carta, vull guanyarte samarro!!! "))

    t=c+1
    
if c>11:
    
    print("O has fet trampa o has guanyat animal de reguerot!!!")
 
elif t>11:
    
    print("He guanyat perroo!!!")