import random

# Realizar un programa que inicialice una lista con 5 
# valores aleatorios (del 1 al 10) y posteriormente que 
# muestre en pantalla cada elemento de la lista junto 
# con sus unidades, decenas y miles.

lista=[ ]
i=0
LONGITUD=5

print("U\tD\tC\tM")

while i < LONGITUD:
    
    lista.append(random.randrange(1,11))

    v1=lista[i]*10
    v2=lista[i]*100
    v3=lista[i]*1000

    print(lista[i],"\t",v1,"\t",v2,"\t",v3)

    i+=1