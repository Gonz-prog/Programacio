import random

#Programa que faça una quiniela aleatòria 
# (busca a Internet com trobar números aleatoris 
# en Python). El programa haurà de mostrar quin 
# símbol posem en cadascuna de les 15 posicions 
# (1, X o 2)


for i in range(1,16,1) :
    
    s=random.randrange(1,4)

    if s==3:

        print("Posicio",i,": X")

    else:

        print("Posicio",i,":",s)