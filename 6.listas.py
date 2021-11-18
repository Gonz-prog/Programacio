# Crear un programa que pida al usuario un número 
# de mes (por ejemplo, el 5) y diga cuántos días 
# tiene (por ejemplo, 31) y el nombre del (mayo). 
# Se deben utilizar listas y supondremos que febrero
# tiene 28 días.

# Crear las listas
meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Introducir datos
numero=int(input("Introduce el numero de un mes: "))

# Con el int introducido recorrer con su valor 
# imprimiendo el str de su posición en las listas
for i in range(numero):
    a=1
print("\n",meses[i],dias[i],"\n")
