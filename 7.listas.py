# Programa para guardar los nombres y la edad de los 
# alumnos de un curso. Hay que pedirlos datos de cada 
# uno por pantalla. La lectura de datos terminará cuando 
# se introduzca como nombre un guión (-) Al terminar se 
# mostrará los siguientes datos:
#•Todos los alumnos mayores de edad.
#•Los dos alumnos más mayores

while True:

    nombre, edad=input("Introduce un nombre o ( - ) para salir: "), int(input("Introduce la edad: "))

    if nombre == " - ":
        
        nombre, edad=input("Introduce un nombre o ( - ) para salir: "), int(input("Introduce la edad: "))
    
    listan=[ ]

    listan.append(nombre)

    listae=[ ]

    listae.append(edad)

    ordeno=listan.copy()
    
    orded=listae.copy()

    ordeno.sort()
    
    orded.sort()

    print("Todos los alumnos mayores de edad:",orded)
    print("Los dos alumnos más mayores:",ordeno[0,1],orded[0,1])