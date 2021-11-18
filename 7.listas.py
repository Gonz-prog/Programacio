# Programa para guardar los nombres y la edad de los 
# alumnos de un curso. Hay que pedirlos datos de cada 
# uno por pantalla. La lectura de datos terminará cuando 
# se introduzca como nombre un guión (-) Al terminar se 
# mostrará los siguientes datos:
# •Todos los alumnos mayores de edad.
# •Los dos alumnos más mayores

# Declaración de variables (Listas)
nombres=[]
edades=[]
orden=[]

# Inicio del programa 
while True:

    # Introducción de datos (nombres)
    nombre=input("Introduce un nombre o ( - ) para salir: ")
    
    # Fin del programa si se cumple la condición
    if nombre == "-":
        break
    
    # Introducción de datos (edades)
    edad=int(input("Introduce la edad: "))
    
    # Introducción de los datos en las listas
    nombres.append(nombre)
    edades.append(edad)

# Imprimimos antes del bucle para no repetir esta frase
print("Todos los alumnos mayores de edad\n")

# Bucle para recorrer la lista de las edades para extraer los mayores de edad
for i in range(len(edades)):
    if edades[i] >= 18:
        print(nombres[i],edades[i],"\n")
    
# Extraer los dos más mayores

# Copiar la lista para no modificar la primera
orden=edades.copy()

# Invertir su orden para tener los valores superiores al principio
orden.sort(reverse=True)

# Indicar la posición de los valores en la lista orden 
# para extraer el valor de la posición de la lista edades
posicio0=edades.index(orden[0])
posicio1=edades.index(orden[1],posicio0+1)

# Imprimimos por pantalla
print("Los dos mas mayores\n")
print(nombres[posicio0],edades[posicio0],nombres[posicio1],edades[posicio1])
