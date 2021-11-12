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

nombres=[]

horas_extra=[]

total_extra=[]

while True:

    nom=input("Nombre ('s' para salir): \n")

    if nom == "s":
        break

    nombres.append(nom)

    acumulador=0

    for i in range(4):

        h=int(input("Horas extras semana "+str(i+1)+": \n"))

        horas_extra.append(h)

        acumulador+=h

    total_extra.append(acumulador)

for i in range(len(total_extra)):
    
    print("\nTrabajador:",nombres[i])

    print("Total horas extras:",total_extra[i])

    print("Total a percibir:",total_extra[i]*11.25,"€\n")