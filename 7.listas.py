# Programa para guardar los nombres y la edad de los 
# alumnos de un curso. Hay que pedirlos datos de cada 
# uno por pantalla. La lectura de datos terminará cuando 
# se introduzca como nombre un guión (-) Al terminar se 
# mostrará los siguientes datos:
#•Todos los alumnos mayores de edad.
#•Los dos alumnos más mayores

nombres=[ ]
edades=[ ]


while True:

    nombre=input("Introduce un nombre o ( - ) para salir: ")

    if nombre == "-":
        break

    edad=int(input("Introduce la edad: "))

    nombres.append(nombre)

    edades.append(edad)

ordeno=nombres.copy()
    
orded=edades.copy()

ordeno.sort()
    
orded.sort()

ordeno.reverse()

orded.reverse()

print("Todos los alumnos mayores de edad:",ordeno[0],ordeno[1])
print("Los dos alumnos más mayores:",ordeno[0],ordeno[1],orded[0],orded[1])
