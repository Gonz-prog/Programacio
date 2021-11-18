# En una empresa de aluminio se quiere guardar el nombre 
# de los trabajadores que tiene (habrá que preguntar), 
# y las horas extras que hacen cada semana. Para guardar 
# esta información se utilizarán dos listas:
# •Nombres: Para guardar los nombres de los trabajadores.
# •Horas: Para guardar las horas extras de la semana 
# (para un mes). Se quiere generar una nueva lista 
# («total_extras») con los total_extra que hace cada 
# trabajador. Supondremos que la hora extra se paga 
# a 11.25€. Al terminar se mostrará la lista con los 
# nombres de los trabajadores y la cantidad extra que 
# será un suplemento en su nómina.

# Iniciar listas
nombres=[]
horas_extra=[]
total_extra=[]

# Iniciar programa
while True:
    
    # Introducir datos
    nom=input("Nombre ('s' para salir): \n")
    
    # Condición de salida
    if nom == "s":
        break
    
    # Insertar el str en la lista nombres
    nombres.append(nom)
    
    # Iniciamos un contador para que sume las horas
    acumulador=0
    
    # Inicio del bucle
    for i in range(4):
        
        # Introduccir de las horas
        h=int(input("Horas extras semana "+str(i+1)+": \n"))
        
        # Insertar los int en la lista horas_extra
        horas_extra.append(h)
        
        # Sumar al acumulador el int
        acumulador+=h
    
    # Insertar a la lista total_exta el valor del acumulador
    total_extra.append(acumulador)
   
# Icicio del bucle que imprimirá cada nombre con sus horas extras
for i in range(len(total_extra)):
    
    print("\nTrabajador:",nombres[i])

    print("Total horas extras:",total_extra[i])

    print("Total a percibir:",total_extra[i]*11.25,"€\n")
