import random

# Realizar un programa que inicialice una lista con 5 
# valores aleatorios (del 1 al 10) y posteriormente que 
# muestre en pantalla cada elemento de la lista junto 
# con sus unidades, decenas y miles.

# Iniciar una lista y las variables
lista=[ ]
i=0
LONGITUD=5

# Imprimir la cabecera tabulada 
print("\nU\tD\tC\tM")

# Inicio bucle hasta 5
while i < LONGITUD:
    
    #Añadir a la lista valores aleatorios entre el 1 y el 10
    lista.append(random.randrange(1,11))

    # Multiplicar cada valor
    v1=lista[i]*10
    v2=lista[i]*100
    v3=lista[i]*1000

    # Imprimir los 5 valores aleatorios
    # con sus productos 
    print(lista[i],"\t",v1,"\t",v2,"\t",v3)

    # Augmentar la variable del bucle en 1 
    # para pasar al siguiente valor aleatorio
    i+=1

#Imprimir una tabulación al final para que quede separado
print("\n")
